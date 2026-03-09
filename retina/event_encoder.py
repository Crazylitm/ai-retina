"""
Event Vision Encoder (事件视觉编码)

Converts continuous image frames into an event stream similar to
Event Cameras (DVS). Each event is a tuple:
    (x, y, timestamp, polarity)
where polarity = +1 (brightening) or -1 (darkening).
"""

import numpy as np


def encode_events(current_frame, previous_frame, threshold=10, timestamp=0.0):
    """Encode frame differences as an event stream.

    Args:
        current_frame: Current grayscale frame.
        previous_frame: Previous grayscale frame.
        threshold: Minimum brightness change to generate an event.
        timestamp: Current timestamp in seconds.

    Returns:
        List of events, each as (x, y, timestamp, polarity).
    """
    diff = current_frame.astype(np.int16) - previous_frame.astype(np.int16)

    events = []

    # ON events (brightening): polarity +1
    on_ys, on_xs = np.where(diff > threshold)
    for x, y in zip(on_xs, on_ys):
        events.append((int(x), int(y), timestamp, 1))

    # OFF events (darkening): polarity -1
    off_ys, off_xs = np.where(diff < -threshold)
    for x, y in zip(off_xs, off_ys):
        events.append((int(x), int(y), timestamp, -1))

    return events


def render_events(events, shape):
    """Render events as a color image for visualization.

    Args:
        events: List of (x, y, timestamp, polarity) tuples.
        shape: (height, width) of the output image.

    Returns:
        BGR image with ON events in green and OFF events in red.
    """
    canvas = np.zeros((shape[0], shape[1], 3), dtype=np.uint8)

    for x, y, _, polarity in events:
        if 0 <= y < shape[0] and 0 <= x < shape[1]:
            if polarity > 0:
                canvas[y, x] = (0, 255, 0)   # Green = ON (brighter)
            else:
                canvas[y, x] = (0, 0, 255)   # Red = OFF (darker)

    return canvas
