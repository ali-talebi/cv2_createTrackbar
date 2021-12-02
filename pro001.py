import cv2 
import numpy as np 

cap = cv2.VideoCapture(1)

def empty(a):
    pass 

cv2.namedWindow('Tracke')
cv2.resizeWindow('Tracke' , 640 , 580)
cv2.createTrackbar('H min' , 'Tracke' ,  0 , 179   ,empty )
cv2.createTrackbar('H max' , 'Tracke' ,  179 , 179 ,empty )
cv2.createTrackbar('S min' , 'Tracke' ,  0 , 179   ,empty )
cv2.createTrackbar('S max' , 'Tracke' ,  179 , 179 ,empty )
cv2.createTrackbar('V min' , 'Tracke' ,  0 , 179   ,empty )
cv2.createTrackbar('V max' , 'Tracke' ,  179 , 179 ,empty )



while True : 

    h_min = cv2.getTrackbarPos('H min' , 'Tracke'  )
    h_max = cv2.getTrackbarPos('H max' , 'Tracke' )
    s_min = cv2.getTrackbarPos('S min' , 'Tracke' )
    s_max = cv2.getTrackbarPos('S max' , 'Tracke' )
    v_min = cv2.getTrackbarPos('V min' , 'Tracke' )
    v_max = cv2.getTrackbarPos('V max' , 'Tracke' )


    ret , frame = cap.read()
    HSV_img = cv2.cvtColor(frame , cv2.COLOR_BGR2HSV )

    lower = np.array([h_min,s_min , v_min ])
    upper = np.array([h_max,s_max , v_max ])

    mask = cv2.inRange(HSV_img , lower , upper )
    result = cv2.bitwise_and(frame , frame , mask=mask )


    cv2.imshow('frame' , frame )
    cv2.imshow('mask' , mask )
    cv2.imshow('result' , result )

    if cv2.waitKey(1) & 0xff==ord('q') : 
        break  

cv2.destroyAllWindows()
cap.release()