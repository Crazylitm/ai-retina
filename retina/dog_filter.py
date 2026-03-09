"""
Center-Surround Receptive Field Filter (中心-周围感受野)

Implements Difference of Gaussian (DoG) filtering to simulate
the spatial contrast enhancement performed by retinal ganglion cells.
"""

import cv2
import numpy as np


def apply_dog_filter(frame, sigma_center=1.0, sigma_surround=3.0):
    """Apply Difference of Gaussian filter to a frame.

    Args:
        frame: Input grayscale image (numpy array).
        sigma_center: Sigma for the center Gaussian.
        sigma_surround: Sigma for the surround Gaussian.

    Returns:
        DoG-filtered image highlighting edges and suppressing flat regions.
    """
    # Compute kernel sizes (must be odd)
    ksize_center = int(6 * sigma_center + 1) | 1
    ksize_surround = int(6 * sigma_surround + 1) | 1

    # Apply Gaussian blurs
    center = cv2.GaussianBlur(frame.astype(np.float64),
                              (ksize_center, ksize_center), sigma_center)
    surround = cv2.GaussianBlur(frame.astype(np.float64),
                                (ksize_surround, ksize_surround), sigma_surround)

    # DoG = center - surround
    dog = center - surround

    return dog
