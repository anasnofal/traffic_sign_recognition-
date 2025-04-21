#!/usr/bin/env python
# coding: utf-8

import argparse
import cv2
from matplotlib import pyplot as plt


ap = argparse.ArgumentParser()

ap.add_argument("-v", "--input", required=True,help="path to input")
ap.add_argument("-s", "--speed", required=True,help="path to speed model")
ap.add_argument("-i", "--stop", required= True,help = " path to model" )
ap.add_argument("-b", "--bump",required= True,help = " path to model")
ap.add_argument("-o", "--output", default="output.mp4", help="Path to save annotated video")

args = vars(ap.parse_args())
# algorithms

speed_limit_signs = cv2.CascadeClassifier(args['speed'])
stop_signs = cv2.CascadeClassifier(args['stop'])
bump_signs = cv2.CascadeClassifier(args['bump'])


# open Video
cap = cv2.VideoCapture(args['input'])
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

# Output video writer
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(args['output'], fourcc, fps, (width, height))

while cap.isOpened():
    ret , frame = cap.read()
    if not ret:
        print("Error: Failed to read frame from video.")
        break
    # convert to gray
    gray = cv2.cvtColor(frame  , cv2.COLOR_BGR2GRAY)
    
    dic = {speed_limit_signs:'SPEED' , stop_signs:'STOP' , bump_signs:'BUMP'}

    # signs detection
    for key_of_dic in dic:
        signs = key_of_dic.detectMultiScale(gray  ,  minSize =(20, 20) ,  minNeighbors =10)
        
        for (x,y,w,h) in signs:
            # create a rectangle
            cv2.rectangle(frame  , (x,y) , (x+w , y+h) , (255,0,0) ,3)
            
            # create a text
            
            cv2.putText(frame  ,str(dic[key_of_dic]) , (x-10,y-10) ,cv2.FONT_HERSHEY_COMPLEX_SMALL, 1 ,(100,0,0) , 2 , cv2.LINE_AA )

    out.write(frame)
    
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

