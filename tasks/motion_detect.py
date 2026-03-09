"""
Motion Detection Validation Task (运动目标检测验证)

Compares two approaches:
  Method A: Direct raw video processing.
  Method B: AI Retina preprocessed output (edges, ON/OFF, events).

Evaluates: stability, lighting robustness, computational cost.
"""


def run_comparison(video_source=0):
    """Run motion detection comparison between raw and retina-processed video.

    Args:
        video_source: Camera index or video file path.
    """
    # TODO: Implement comparison task
    # 1. Capture frames from video_source
    # 2. Method A: detect motion on raw frames
    # 3. Method B: run AI Retina pipeline, detect motion on output
    # 4. Compare metrics: stability, lighting robustness, compute time
    raise NotImplementedError("Implement motion detection comparison")
