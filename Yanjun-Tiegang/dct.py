import cv2
import numpy as np
from points import pointsInsideCircle
from math import pi as PI
W = 16


img = cv2.imread("boredom.jpg",0)
imgcv1 = cv2.split(img)[0]
#cv2.imshow("display",imgcv1)
imgcv2 = cv2.imread("boredom.png")
cv2.boxFilter(imgcv1, cv2.IPL_DEPTH_32F, (7,7), imgcv2, (-1,-1), False, cv2.BORDER_DEFAULT)
#cv2.imshow("display_2",imgcv2)
#key = cv2.waitKey(0)&0xFF
#if key == ord('q'):
#		cv2.destroyAllwindows()
#imgcv2 = cv2.resize(imgcv1,(64,64))

height,width = img.shape[:2]
"""
cv2.imshow("display_2",imgcv2)
key = cv2.waitKey(0)&0xFF
if key == 27:
cv2.destroyAllWindows()
"""
h=0;i=0;index=-1;
blocks = []
points = pointsInsideCircle(W)
#Moving block of size WxW over image
for h in range(0,height+1-W):
	for i in range(0,width+1-W):
		index = index + 1
		temp = {}
		temp['index'] = index
		j=0;
		temp_img_list = []
		#forming block of size WxW from img
		for j in range(0,W):
			temp_img_list.append(img[h+j][i:i+W])
			#applying DCT on WxW size block
		temp_block = np.float32(temp_img_list)
		dstion = cv2.dct(temp_block)
		temp['dct'] = dstion
		#forming feature vector from block
		feature_vector = []
		for key,points_list in points.iteritems():

			summation = 0
			for dct_pos in points_list:
				summation = summation + dstion[dct_pos[0],dct_pos[1]]	
			feature_value = summation/(PI*W*W)
			feature_vector.append(feature_value)
		print feature_vector	
