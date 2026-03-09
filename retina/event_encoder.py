"""
Event Vision Encoder (事件视觉编码)

Converts continuous image frames into an event stream similar to
Event Cameras (DVS). Each event is a tuple:
    (x, y, timestamp, polarity)
where polarity = +1 (brightening) or -1 (darkening).
"""


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
    # TODO: Implement event encoding
    # 1. Compute difference: current - previous
    # 2. For each pixel exceeding +threshold: emit event with polarity +1
    # 3. For each pixel exceeding -threshold: emit event with polarity -1
    # 4. Return list of (x, y, timestamp, polarity) tuples
    raise NotImplementedError("Step 4: Implement event encoder")
