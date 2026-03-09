"""
Center-Surround Receptive Field Filter (中心-周围感受野)

Implements Difference of Gaussian (DoG) filtering to simulate
the spatial contrast enhancement performed by retinal ganglion cells.
"""


def apply_dog_filter(frame, sigma_center=1.0, sigma_surround=3.0):
    """Apply Difference of Gaussian filter to a frame.

    Args:
        frame: Input grayscale image (numpy array).
        sigma_center: Sigma for the center Gaussian.
        sigma_surround: Sigma for the surround Gaussian.

    Returns:
        DoG-filtered image highlighting edges and suppressing flat regions.
    """
    # TODO: Implement DoG filter
    # 1. Apply Gaussian blur with sigma_center
    # 2. Apply Gaussian blur with sigma_surround
    # 3. Return difference (center - surround)
    raise NotImplementedError("Step 1: Implement DoG filter")
