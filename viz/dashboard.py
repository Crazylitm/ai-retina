"""
Visualization Dashboard (可视化面板)

Displays multiple retina processing channels side by side:
- Original image
- DoG edge map
- ON channel
- OFF / Motion
- Event stream visualization
"""

import cv2
import numpy as np


def _add_label(image, label):
    """Add a text label to the top-left of an image."""
    cv2.putText(image, label, (10, 25),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
    return image


def _to_bgr(gray):
    """Convert single-channel to 3-channel BGR for stacking."""
    if len(gray.shape) == 2:
        return cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
    return gray


def create_dashboard(original, dog_output, on_channel, off_channel, event_image):
    """Create a multi-panel visualization dashboard.

    Args:
        original: Original camera frame (BGR).
        dog_output: DoG filter output (grayscale, float or uint8).
        on_channel: ON channel output (grayscale uint8).
        off_channel: OFF channel output (grayscale uint8).
        event_image: Event visualization image (BGR).

    Returns:
        Combined dashboard image for display.
    """
    h, w = original.shape[:2]
    panel_size = (w // 2, h // 2)

    # Resize all panels
    p_original = cv2.resize(original, panel_size)
    _add_label(p_original, "Original")

    # Normalize DoG for display
    from retina.utils import normalize
    dog_norm = normalize(dog_output)
    p_dog = cv2.resize(_to_bgr(dog_norm), panel_size)
    _add_label(p_dog, "DoG Edges")

    # ON channel (green tint)
    on_bgr = np.zeros((on_channel.shape[0], on_channel.shape[1], 3), dtype=np.uint8)
    on_bgr[:, :, 1] = on_channel  # Green channel
    p_on = cv2.resize(on_bgr, panel_size)
    _add_label(p_on, "ON (Brighter)")

    # OFF channel (red tint)
    off_bgr = np.zeros((off_channel.shape[0], off_channel.shape[1], 3), dtype=np.uint8)
    off_bgr[:, :, 2] = off_channel  # Red channel
    p_off = cv2.resize(off_bgr, panel_size)
    _add_label(p_off, "OFF (Darker)")

    # Events
    p_events = cv2.resize(event_image, panel_size)
    _add_label(p_events, "Events")

    # FPS/info panel
    p_info = np.zeros((panel_size[1], panel_size[0], 3), dtype=np.uint8)
    cv2.putText(p_info, "AI Retina v1", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 200, 255), 2)
    cv2.putText(p_info, "Press 'q' to quit", (10, 60),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (150, 150, 150), 1)

    # Arrange in 2x3 grid
    top_row = np.hstack([p_original, p_dog, p_on])
    bottom_row = np.hstack([p_off, p_events, p_info])
    dashboard = np.vstack([top_row, bottom_row])

    return dashboard
