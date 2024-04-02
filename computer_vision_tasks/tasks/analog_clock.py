import cv2
import datetime
import math

#import the attributes
from constants import COLORS
from constants import RADIUS
from constants import CENTER


#get theposition of ticks from the function
def get_ticks():
	hours_init = []
	hours_dest = []
@@ -23,6 +28,7 @@ def get_ticks():

	return hours_init, hours_dest

#Turn time into suitable representation
def getDigitalTime(h,m,s):
	time = ""
	hour = ""
@@ -43,7 +49,10 @@ def getDigitalTime(h,m,s):
	time = hour+minute+second
	return time

#Function for drawing the hands of teh clock
def draw_time(image):

	#getting the time from time module 
	time_now = datetime.datetime.now().time()
	hour = math.fmod(time_now.hour, 12)
	minute = time_now.minute
 11  
analog_clock.py
@@ -1,27 +1,38 @@
#Import the dependecies
import cv2
import numpy as np

#Import the required attributes and helper functions
from constants import COLORS, CANVAS_SIZE, RADIUS
from HelperFunctions import get_ticks, draw_time

#Make a empty canvas
image = np.zeros(CANVAS_SIZE, dtype=np.uint8)
#Turn it to white color
image[:] = [255,255,255]

#get the starting and ending points of ticks in the watch
hours_init, hours_dest = get_ticks()

#Draw all the ticks using for loop
for i in range(len(hours_init)):
	if i % 5 == 0:
		cv2.line(image, hours_init[i], hours_dest[i], COLORS['black'], 3)
	else:
		cv2.circle(image, hours_init[i], 5, COLORS['gray'], -1)

#Draw some decorations on the watch
cv2.circle(image, (320,320), RADIUS+10, COLORS['yellow'], 2)
cv2.putText(image, "TITAN", (215,230), cv2.FONT_HERSHEY_TRIPLEX, 2, COLORS['dark_gray'], 1, cv2.LINE_AA)

#Run until user stops
while True:
	image_original = image.copy()

	#Use draw time to make clock hands on the canvas
	clock_face = draw_time(image_original)

	#Show the watch
	cv2.imshow('clock', image_original)
	if(cv2.waitKey(1)==ord('q')):
		break