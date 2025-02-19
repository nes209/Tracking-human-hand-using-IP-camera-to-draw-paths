# Human Hand Tracking Project Using IP Camera to Draw Paths:

This project uses the cvzone hand tracking library with OpenCV library to capture video from IP camera 
and display hand movement tracking. The program detects the hand and tracks the index finger movement to
draw paths created by the user in real time.

## Main functions:
* Capture video from IP camera via specified URL.
* Tracking hand movement using HandDetector library from cvzone.
* Drawing paths based on index finger movement.
* Reset path when 'n' key is pressed.
* Close program when 'q' key is pressed.

## How to use:

### Make sure the IP camera is turned on:
Make sure the IP Webcam application is turned on on the phone or camera, and use the correct address in the url variable (eg: "http://192.168.217.141:8080/video").

### Run the program:
When the program is started, it starts capturing video from the IP camera and displays the image with paths drawn based on the hand movement.

### Reset the path:
When you press 'n', the current path is cleared and a new path is drawn.

### Close the program:
When you press 'q', the program is closed.

## Project libraries and components:
* cv2: To use OpenCV for video interaction and image processing.

* cvzone: To use HandTrackingModule which enables hand tracking.

