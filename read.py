import cv2
import numpy as np
from matplotlib import pyplot
import matplotlib.pyplot as plt
import math

pi = math.pi
threshold = 190    #210#threshold  n. 入口；门槛；开始；极限；临界值


for i in range(0,691):
    img = cv2.imread("/home/robo/catkin_ws/src/sadahira_test/data/image/{0:03d}.png".format(i))
    #gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    lower_white = np.array([0,210,0])
    upper_white = np.array([180,255,255])
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HLS)
    img_range = cv2.inRange(img_hsv,lower_white,upper_white)
    #ret, img_thresh = cv2.threshold(gray, threshold, 255, cv2.THRESH_BINARY)
   # cv2.imwrite("/home/robo/catkin_ws/src/sadahira_test/data/image_output_wpx/gray{0:03d}(%d).png".format(i),img_thresh)

    #lines = cv2.HoughLinesP(img_thresh, rho=1, theta=np.pi/360, threshold=130,    
    #minLineLength=30,maxLineGap=50)
    lines = cv2.HoughLinesP(img_range, rho=1, theta=np.pi/360, threshold=130,    
    minLineLength=30,maxLineGap=50)

    long_x = 0 
    long_y = 0
    for line in lines:   #yoko
        x1, y1, x2, y2 = line[0]
	slope_x = abs((y2-y1) / (x2-x1))
	slope_y = abs((x2-x1) / (y2-y1))
        red_line_img = cv2.line(img, (x1,y1), (x2,y2), (0,0,255), 3)
        
    
        if (long_x < x2-x1) and (slope_x < 0.5):
           long_x = x2-x1
	   
           x1max = x1
           x2max = x2
           y1max = y1
           y2max = y2 
 
           print(x1max,x2max,y1max,y2max)

	#if (long_y < y2-y1) and (slope_y < 0.5):
	   #long_y = y2-y1

	   #x1min = x1
	   #x2min = x2
   	   #y1min = y1
 	   #y2min = y2
           #print(x1min,x2min,y1min,y2min)
        #else:
            #print("non")
            

    a = math.atan2((y2max-y1max),long_x)   
    img = cv2.line(img,(x1max,y1max),(x2max,y2max),(255,0,0),3)
    #img = cv2.line(img,(x1min,y1min),(x2min,y2min),(0,255,0),3)
     


    cv2.imwrite("/home/robo/catkin_ws/src/sadahira_test/data/image_output_wpx2/{0:03d}(%f).png".format(i)  %a,img)

    print("/home/robo/catkin_ws/src/sadahira_test/data/image_output_wpx2{0:03d}(%d).png".format(i)%a)


