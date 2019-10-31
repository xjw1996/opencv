import cv2
import numpy as np
from matplotlib import pyplot #绘图库
import matplotlib.pyplot as plt
import math

pi = math.pi
threshold = 190    #210


for i in range(0,691):
    img = cv2.imread("/home/robo/catkin_ws/src/sadahira_test/data/image/{0:03d}.png".format(i))
    #0:03d 位数补0
    # o是被填充到缺省位的数字，3代表规定数字的总位数  d代表是整型。
    #gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    lower_white = np.array([0,180,0])
    upper_white = np.array([180,255,255])
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HLS)
    img_range = cv2.inRange(img_hsv,lower_white,upper_white)
    
    cv2.imwrite("/home/robo/catkin_ws/src/sadahira_test/data/hsv/{0:03d}.png".format(i)  ,img_range)
   
