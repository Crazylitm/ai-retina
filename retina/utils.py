"""
Utility functions for AI Retina.
"""

import cv2
import numpy as np


def to_grayscale(frame):
    """Convert a BGR frame to grayscale."""
    if len(frame.shape) == 2:
        return frame
    return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


def normalize(image):
    """Normalize image to 0-255 range for display."""
    img = image.astype(np.float64)
    min_val = img.min()
    max_val = img.max()
    if max_val - min_val == 0:
        return np.zeros_like(image, dtype=np.uint8)
    normalized = ((img - min_val) / (max_val - min_val) * 255).astype(np.uint8)
    return normalized
