#!/usr/bin/env python
# coding: utf-8

# In[2]:


import cv2
from matplotlib import pyplot as plt


# In[16]:


# algorithms

speed_limit_signs = cv2.CascadeClassifier('E:/Traffic Sign Detection/haarCascade.xml')
stop_signs = cv2.CascadeClassifier('E:/Traffic Sign Detection/Stopsigns.xml')
bump_signs = cv2.CascadeClassifier('E:/Traffic Sign Detection/bump_signs.xml')


# In[53]:


# open image

img  = cv2.imread('E:/Traffic Sign Detection/archive/images/data of traffic signs/p/road328.png')
img = cv2.cvtColor(img  , cv2.COLOR_BGR2RGB)

# convert to gray
gray = cv2.cvtColor(img  , cv2.COLOR_RGB2GRAY)

# signs detection
dic = {speed_limit_signs:'SPEED' , stop_signs:'STOP' , bump_signs:'BUMP'}

for key_of_dic in dic:
    
    signs = key_of_dic.detectMultiScale(gray  ,  minSize =(20, 20) , minNeighbors =2)
    
    # create a rectangle
    for (x,y,w,h) in signs:
        cv2.rectangle(img  , (x,y) , (x+w , y+h) , (255,0,0) ,3)
        # create a text

        cv2.putText(img  , str(dic[key_of_dic]), (x-10,y-10) ,cv2.FONT_HERSHEY_COMPLEX_SMALL , 1 ,(100,0,0) , 2 , cv2.LINE_AA )
    

plt.imshow(img)
plt.show()
# cv2.imshow('img ' , img)


# In[54]:


# open Video
cap = cv2.VideoCapture('E:/Traffic Sign Detection/Ford Focus - Traffic Sign Recognition_Trim.mp4')

while cap.isOpened():
   
    __ , frame = cap.read()

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
   
    cv2.imshow('Traffic Signs Detection' , frame)
    
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

