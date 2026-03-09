"""
AI Retina - Main Entry Point (主程序)

Captures video from camera and runs the biomimetic retina pipeline:
  1. Center-Surround (DoG) filtering
  2. ON/OFF channel separation
  3. Temporal change detection
  4. Event stream encoding
  5. Dashboard visualization
"""


def main():
    """Run the AI Retina pipeline on live camera input."""
    print("AI Retina - Biomimetic Vision Frontend")
    print("=" * 40)
    print()
    print("Modules to implement:")
    print("  1. retina/dog_filter.py   - Center-Surround (DoG)")
    print("  2. retina/on_off.py       - ON/OFF Channels")
    print("  3. retina/temporal.py     - Temporal Change Detection")
    print("  4. retina/event_encoder.py - Event Stream Encoding")
    print("  5. viz/dashboard.py       - Visualization Dashboard")
    print()
    print("Start with Step 1: implement dog_filter.py")

    # TODO: Once modules are implemented:
    # 1. Open camera with cv2.VideoCapture(0)
    # 2. Read frames in a loop
    # 3. Convert to grayscale
    # 4. Apply DoG filter
    # 5. Compute ON/OFF channels
    # 6. Detect temporal changes
    # 7. Encode events
    # 8. Display dashboard
    # 9. Break on 'q' key press


if __name__ == "__main__":
    main()
