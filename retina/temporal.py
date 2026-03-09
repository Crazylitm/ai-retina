"""
Temporal Change Detection (时间变化检测)

Detects changes in the visual scene over time by computing
frame differences, highlighting moving objects and suppressing
static backgrounds.
"""


def detect_temporal_change(current_frame, previous_frame, threshold=15):
    """Detect temporal changes between consecutive frames.

    Args:
        current_frame: Current grayscale frame.
        previous_frame: Previous grayscale frame.
        threshold: Minimum pixel difference to count as change.

    Returns:
        Binary mask of changed regions.
    """
    # TODO: Implement temporal change detection
    # 1. Compute absolute difference |frame(t) - frame(t-1)|
    # 2. Apply threshold to get binary change mask
    # 3. Optionally apply morphological operations to clean up noise
    raise NotImplementedError("Step 3: Implement temporal change detection")
