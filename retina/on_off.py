"""
ON / OFF Channels (ON / OFF 通道)

Simulates the retina's dual-pathway processing for brightness changes.
ON channel responds to brightening; OFF channel responds to darkening.
"""


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
    # TODO: Implement ON/OFF channels
    # 1. Compute difference: current - previous
    # 2. ON channel = max(difference, 0)   -> brightening
    # 3. OFF channel = max(-difference, 0) -> darkening
    raise NotImplementedError("Step 2: Implement ON/OFF channels")
