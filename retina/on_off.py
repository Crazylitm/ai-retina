"""
ON / OFF Channels (ON / OFF 通道)

Simulates the retina's dual-pathway processing for brightness changes.
ON channel responds to brightening; OFF channel responds to darkening.
"""

import numpy as np


def compute_on_off_channels(current_frame, previous_frame):
    """Compute ON and OFF channels from consecutive frames.

    Args:
        current_frame: Current grayscale frame.
        previous_frame: Previous grayscale frame.

    Returns:
        Tuple of (on_channel, off_channel) arrays.
        on_channel: regions that got brighter (polarity +1).
        off_channel: regions that got darker (polarity -1).
    """
    diff = current_frame.astype(np.float64) - previous_frame.astype(np.float64)

    # ON channel: brightening (positive changes)
    on_channel = np.clip(diff, 0, 255).astype(np.uint8)

    # OFF channel: darkening (negative changes, shown as positive values)
    off_channel = np.clip(-diff, 0, 255).astype(np.uint8)

    return on_channel, off_channel
