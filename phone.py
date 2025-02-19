import cv2
from cvzone.HandTrackingModule import HandDetector

url = "http://192.168.217.141:8080/video"  
cap = cv2.VideoCapture(url)


if not cap.isOpened():
    print("Camera connection error!")
    print("Make sure IP Webcam is turned on and both devices are on the same network")
    exit()

detector = HandDetector(maxHands=1, detectionCon=0.7)
segments = []
current_segment = []

while True:
    success, img = cap.read()
    if not success:
        continue

    img = cv2.flip(img, 1)  
    hands, img = detector.findHands(img, draw=True)

    key = cv2.waitKey(1)
    if key == ord('n'):
        segments.clear()
        current_segment.clear()

    if hands:
        hand = hands[0]
        lmList = hand["lmList"]
        
        if len(lmList) >= 21:
            
            x, y = lmList[8][0], lmList[8][1]
            current_segment.append((x, y))

 
    for segment in segments:
        if len(segment) > 1:
            for i in range(1, len(segment)):
                cv2.line(img, segment[i-1], segment[i], (0,0,255), 5)

 
    if len(current_segment) > 1:
        for i in range(1, len(current_segment)):
            cv2.line(img, current_segment[i-1], current_segment[i], (0,0,255), 5)

    cv2.imshow("Hand Drawing", img)
    
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()