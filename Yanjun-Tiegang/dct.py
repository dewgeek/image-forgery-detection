import cv2
import numpy as np
from points import pointsInsideCircle
from math import pi as PI
from math import sqrt
from calcIdentical import calcIdentical
W = 16
Dsim = 0.0005
Nd = 8

img = cv2.imread("test.jpg",0)
#output_image = cv2.imread("anushka.jpg",1)

#img = cv2.imread("red.png",0)
imgcv1 = cv2.split(img)[0]
#cv2.imshow("display",imgcv1)
imgcv2 = imgcv1
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

points = pointsInsideCircle(W)
features=[]
#Moving block of size WxW over image
for h in range(0,height+1-W):
	for i in range(0,width+1-W):
		j=0;
		temp_img_list = []
		#forming block of size WxW from img
		for j in range(0,W):
			temp_img_list.append(img[h+j][i:i+W])
			#applying DCT on WxW size block
		temp_block = np.float32(temp_img_list)
		dstion = cv2.dct(temp_block)
		
		#forming feature vector from block
		feature_vector = []
		for key,points_list in points.iteritems():

			summation = 0
			for dct_pos in points_list:
				summation = summation + dstion[dct_pos[0],dct_pos[1]]	
			feature_value = summation/(PI*W*W)
			feature_vector.append(feature_value)
		features.append(feature_vector)
#		if feature_vector[0] != 0.0 or feature_vector[1] != 0.0 or feature_vector[2] != 0.0 or feature_vector[3] != 0.0 :
#			print feature_vector
sorted_features = cv2.sort(np.array(features),cv2.SORT_ASCENDING)
print "Done with feature vectore"
output_list = []
i=0;
for i in range(0,len(sorted_features)):
	j = i;
	for j in range(i,len(sorted_features)):
	

		similiar = calcIdentical(sorted_features[i],sorted_features[j],Dsim,Nd)	
		if similiar:
			x1 = i%width
			y1 = i/width
			x2 = j%width
			y2 = j/width
			
			dist = sqrt((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2))

			if dist > Nd:
				print "match found between ("+str(x1)+","+str(y1)+") and ("+str(x2)+","+str(y2)+")"
				print "feature vectors are "+str(sorted_features[i])+","+str(sorted_features[j])+"."
				output_list.append([sorted_features[i],sorted_features[j]])
				
				output_image = cv2.imread("output.jpg")
				k=0	
				for k in range(0,W):
					output_image[y1+k][x1:x1+W] = [0,0,0]
					output_image[y2+k][x2:x2+W] = [255,255,255]
					k=k+1
				cv2.imwrite("output.jpg",output_image)
			

		j = j+1
	i = i+1
print output_list
