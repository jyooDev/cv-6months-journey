import matplotlib.pyplot as plt
import cv2 as cv
import os

def callback():
    pass

def cannyEdge():
    root = os.getcwd()
    imgPath = os.path.join(root, "data/opt_photo.png")
    img = cv.imread(imgPath)
    img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    
    windowName = 'Canny Window'
    cv.namedWindow(windowName)
    cv.createTrackbar('minThreshold', windowName, 0, 255, callback)    
    cv.createTrackbar('maxThreshold', windowName, 0, 255, callback)    

    while True:
        if cv.waitKey(1) == ord('q'):
            break

        minThreshold = cv.getTrackbarPos('minThreshold', windowName)
        maxThreshold = cv.getTrackbarPos('maxThreshold', windowName)
        edgeImg = cv.Canny(img, minThreshold, maxThreshold)
        print(edgeImg)
        cv.imshow(windowName, edgeImg)

    cv.destroyAllWindows()



if __name__ == "__main__":
    cannyEdge()