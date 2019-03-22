import cv2
import numpy as np
import matplotlib
import statistics
template1 = cv2.imread('green.jpg',0)



capture=cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH,1080)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT,1500)

def find_template(where,picture,threshold=0.3,color=(0,0,255)):
    
    img_gray = cv2.cvtColor(where, cv2.COLOR_BGR2GRAY)

    res = cv2.matchTemplate(img_gray,picture,cv2.TM_CCOEFF_NORMED)
    w, h = picture.shape[::-1]
    
    loc = np.where( res >= threshold)
    print(loc)
    X=[]
    Y=[]
    for pt in zip(*loc[::-1]):
        X.append(pt[0])
        Y.append(pt[1])
    if X==[]:
        return 
    data=int(statistics.median(X)),int(statistics.median(Y))
    cv2.rectangle(where, data, (data[0]+w, data[1] +h), color, 1)   
        
       
while True:
    ret,frame=capture.read()
    image=cv2.cvtColor(frame,cv2.COLOR_BGR2BGRA)
    find_template(image,template1,threshold=0.45)
    image=cv2.flip(image,3)
    
  
   

    cv2.imshow('image',image)
    cv2.waitKey(20)
    

cv2.destroyAllWindows()

