import sys
import cv2
import numpy as np
from utils import pointsInsideCircle, compare, zigzag
from math import pi as PI


W	= 8 			#block size for comparision
Dsim	= 0.1			#threshold for symmetry
Nd	= 25			#nearest block

quadrants_points = pointsInsideCircle(W/4)	#(i,j) position of blocks which are partially/completely inside circle of radius W/2
zigzag_points = zigzag(W/2)
test_image = cv2.imread(sys.argv[1],0)
height,width = test_image.shape[:2]
#print (height,width)
vectors_list = []
for j in range(0,height-W+1):
	for i in range(0,width-W+1):
		block = test_image[j:j+W,i:i+W]
		dct_block =  cv2.dct(np.float32(block))
		feature_block = [[],[],[],[]]
		for index,coeff_list in enumerate(zigzag_points):
			for coeff in coeff_list:
				feature_block[index].append(dct_block[coeff[0],coeff[1]])
			
		feature_block_np = np.array(feature_block)
		
		feature_vector = []
		for quadrant,points in quadrants_points.iteritems():
			summ = 0
			for point in points:
				summ = summ + feature_block_np[point[0],point[1]]
			feature_vector.append(summ/PI)
		vectors_list.append(np.array(feature_vector))
	 
vectors_list2 = cv2.sort(np.array(vectors_list),cv2.SORT_EVERY_ROW)
print "vectors calculated"
import json
with open('data.json', 'w') as outfile:
	json.dump(vectors_list2.tolist(), outfile)


i=0
blocks = []
for i in range(0,len(vectors_list)):
	if i%width == 0:
		print i/width
	posA = [i/width,i%width]
	j = i+1
	for j in range(i+1,len(vectors_list)):
		posB = [j/width,j%width]
		if compare(vectors_list[i],vectors_list[j],posA,posB,Dsim,Nd):
			print (posA,posB)
			blocks.append([posA,posB])

output_image = cv2.imread(sys.argv[1],1)
for block in blocks:
	x1 = block[0][0]
	x1_8 = block[0][0]+W
	y1 = block[0][1]
	y1_8 = block[0][1]+W
	
	output_image[x1:x1_8,y1:y1_8] = [0,0,255]
	
	x2 = block[1][0]
	x2_8 = block[1][0]+W
	y2 = block[1][1]
	y2_8 = block[1][1]+W

	output_image[x2:x2_8,y2:y2_8]=[0,255,0]

cv2.imwrite("output.jpg",output_image)
				
	
print "feature vectors extracted"



