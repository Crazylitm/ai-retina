"""
Temporal Change Detection (时间变化检测)

Detects changes in the visual scene over time by computing
frame differences, highlighting moving objects and suppressing
static backgrounds.
"""

import cv2
import numpy as np


def detect_temporal_change(current_frame, previous_frame, threshold=15):
    """Detect temporal changes between consecutive frames.

    Args:
        current_frame: Current grayscale frame.
        previous_frame: Previous grayscale frame.
        threshold: Minimum pixel difference to count as change.

    Returns:
        Binary mask of changed regions (255 = changed, 0 = static).
    """
    # Absolute difference
    diff = cv2.absdiff(current_frame, previous_frame)

    # Threshold to binary
    _, mask = cv2.threshold(diff, threshold, 255, cv2.THRESH_BINARY)

    # Clean up noise with morphological operations
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_DILATE, kernel)

    return mask
