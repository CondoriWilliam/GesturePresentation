import os
import cv2
import numpy as np
from cvzone.HandTrackingModule import HandDetector

# size of display
width, height = 1920, 1080
folderPath = "Presentation"

# Camera setup
camera = cv2.VideoCapture(0)
camera.set(3, width)
camera.set(4, height)

# Get the list of presentation images
pathImages = sorted(os.listdir(folderPath), key=len)

# Size of video
imgNumber = 0
settingOfDisplay = 2
hs, ws = int(120 * settingOfDisplay), int(213 * settingOfDisplay)
gestureThreshold = int(height/2)
buttonPressed = False
buttonCounter = 0
buttonDelay = 30
annotations = [[]]
annotationNumber = 0
annotationStart = False

# Hand detector
detector = HandDetector(detectionCon=0.8, maxHands=1)

while True:
    # Import images
    success, img = camera.read()
    img = cv2.flip(img, 1)
    pathFullImage = os.path.join(folderPath, pathImages[imgNumber])
    imgCurrent = cv2.imread(pathFullImage)

    hands, img = detector.findHands(img)
    cv2.line(img, (0, gestureThreshold), (width, gestureThreshold), (0, 255, 0), 10)

    if hands and buttonPressed is False:
        hand = hands[0]
        fingers = detector.fingersUp(hand)
        cx, cy = hand['center']
        lmList = hand['lmList']

        # Constrain values for easier drawing
        xVal = int(np.interp(lmList[8][0], [width/2, width], [0, width]))
        yVal = int(np.interp(lmList[8][1], [150, height-150], [0, height]))
        indexFinger = xVal, yVal
        #indexFinger = lmList[8][0], lmList[8][1]

        if cy <= gestureThreshold:
            # Gesture 1 - left
            if fingers == [1,0,0,0,0]:
                if imgNumber > 0:
                    annotations = [[]]
                    annotationNumber = 0
                    annotationStart = False
                    buttonPressed = True
                    imgNumber -= 1

            # Gesture 2 - right
            if fingers == [0,0,0,0,1]:
                if imgNumber < len(pathImages) - 1:
                    annotations = [[]]
                    annotationNumber = 0
                    annotationStart = False
                    buttonPressed = True
                    imgNumber += 1

        # Gesture 3 - Print point
        if fingers == [0,1,1,0,0]:
            cv2.circle(imgCurrent, indexFinger, 12, (0,0,255), cv2.FILLED)

        # Gesture 4 - Draw
        if fingers == [0, 1, 0, 0, 0]:
            if annotationStart is False:
                annotationStart = True
                annotationNumber += 1
                annotations.append([])
            cv2.circle(imgCurrent, indexFinger, 12, (0, 0, 255), cv2.FILLED)
            annotations[annotationNumber].append(indexFinger)
        else:
            annotationStart = False

        # Gesture 5 - Erase
        if fingers == [0, 1, 1, 1, 0]:
            if annotations:
                if annotationNumber >= 0:
                    annotations.pop(-1)
                    annotationNumber -= 1
                    buttonPressed = True

        # Gesture 6 - Close
        if fingers == [1, 1, 1, 1, 1]:
            break

    # iteration button
    if buttonPressed:
        buttonCounter += 1
        if buttonCounter > buttonDelay:
            buttonCounter = 0
            buttonPressed = False

    for i in range(len(annotations)):
        for j in range(len(annotations[i])):
            if j != 0:
                cv2.line(imgCurrent,annotations[i][j-1], annotations[i][j], (0,0,200), 12)

    # Adding webcam image on the slides
    imgSmall = cv2.resize(img, (ws, hs))
    h, w, _ = imgCurrent.shape
    imgCurrent[0:hs, w - ws:w] = imgSmall

    cv2.imshow("Image", img)
    cv2.imshow("Slides", imgCurrent)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break






















