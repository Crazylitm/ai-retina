"""
AI Retina - Main Entry Point (主程序)

Captures video from camera and runs the biomimetic retina pipeline:
  1. Center-Surround (DoG) filtering
  2. ON/OFF channel separation
  3. Temporal change detection
  4. Event stream encoding
  5. Dashboard visualization

Usage:
    python3 main.py           # Use default camera (index 0)
    python3 main.py --cam 1   # Use camera index 1
"""

import sys
import time
import cv2
import numpy as np

from retina.utils import to_grayscale
from retina.dog_filter import apply_dog_filter
from retina.on_off import compute_on_off_channels
from retina.temporal import detect_temporal_change
from retina.event_encoder import encode_events, render_events
from viz.dashboard import create_dashboard


def main():
    """Run the AI Retina pipeline on live camera input."""
    # Parse camera index from args
    cam_index = 0
    if "--cam" in sys.argv:
        idx = sys.argv.index("--cam")
        if idx + 1 < len(sys.argv):
            cam_index = int(sys.argv[idx + 1])

    print("AI Retina - Biomimetic Vision Frontend")
    print("=" * 40)
    print(f"Opening camera {cam_index}...")

    cap = cv2.VideoCapture(cam_index)
    if not cap.isOpened():
        print(f"Error: Cannot open camera {cam_index}")
        print("Try: python3 main.py --cam 1")
        sys.exit(1)

    # Read first frame to initialize
    ret, frame = cap.read()
    if not ret:
        print("Error: Cannot read from camera")
        cap.release()
        sys.exit(1)

    prev_gray = to_grayscale(frame)
    frame_count = 0
    start_time = time.time()

    print(f"Camera opened: {frame.shape[1]}x{frame.shape[0]}")
    print("Press 'q' to quit")
    print()

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Convert to grayscale
        gray = to_grayscale(frame)

        # 1. DoG filter (center-surround)
        dog_output = apply_dog_filter(gray)

        # 2. ON/OFF channels
        on_channel, off_channel = compute_on_off_channels(gray, prev_gray)

        # 3. Temporal change detection
        motion_mask = detect_temporal_change(gray, prev_gray)

        # 4. Event encoding
        elapsed = time.time() - start_time
        events = encode_events(gray, prev_gray, threshold=10, timestamp=elapsed)
        event_image = render_events(events, gray.shape)

        # 5. Dashboard
        dashboard = create_dashboard(
            frame, dog_output, on_channel, off_channel, event_image
        )

        # Add FPS counter
        frame_count += 1
        fps = frame_count / (time.time() - start_time) if time.time() > start_time else 0
        cv2.putText(dashboard, f"FPS: {fps:.1f} | Events: {len(events)}",
                    (10, dashboard.shape[0] - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

        # Display
        cv2.imshow("AI Retina", dashboard)

        # Update previous frame
        prev_gray = gray.copy()

        # Quit on 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    print(f"\nProcessed {frame_count} frames in {time.time() - start_time:.1f}s")
    print(f"Average FPS: {frame_count / (time.time() - start_time):.1f}")


if __name__ == "__main__":
    main()
