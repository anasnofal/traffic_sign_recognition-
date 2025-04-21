# Traffic Sign Detection with Custom Haar Cascades

This project performs traffic sign detection using custom Haar Cascade classifiers. The classifiers are specifically trained to detect speed limit signs, stop signs, and bump signs from input video files. The annotated output is saved as a video with bounding boxes and labels for each detected sign.

## Features
- Detects and labels traffic signs (Speed Limit, Stop, and Bump) using Haar Cascade classifiers.
- Processes input video and saves the output with annotations (bounding boxes and labels).
- Custom-trained Haar cascades for better accuracy in detecting the specific signs.
  
## Prerequisites
Ensure you have the following dependencies installed:
- Python 3.x
- OpenCV
- Matplotlib

You can install the required dependencies using `pip` by running:
```bash
pip install opencv-python matplotlib
 ```
 then run this command 

 ```
 python Traffic-Sign-Detection.py -v input_video.mp4 -s speed_limit_signs.xml -i stop_signs.xml -b bump_signs.xml -o output_video.mp4

```