#The two main libaries we need are:
#1.opencv
#2.cvzone 
import cv2
from cvzone.PoseModule import PoseDetector


video = cv2.VideoCapture(0)
#create a variable that stores the attribute PoseDetector
detect = PoseDetector()

while True:
    ret,frame = video.read()
    image_reading = detect.findPose(frame) #getting the position on the image/frame
    body,box_reading = detect.findPosition(frame,bboxWithHands=False)

    #Now, lets check the center of each coordinate in the human body
    if box_reading:
        center = box_reading['center']
        #lets draw and give a crircle mark at each joint movement of the body
        cv2.circle(frame,center,5,(255,255,0),cv2.FILLED)

    cv2.imshow('farme_name',frame)

    if cv2.waitKey(20) and 0xFF == ord('q'):
        break
video.release()
cv2.destroyAllWindows()