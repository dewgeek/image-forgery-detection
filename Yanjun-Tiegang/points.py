from random import randrange
import numpy as np
from math import sqrt

"""



"""


def pointsInsideCircle(radius):
	W = radius
	i=0;j=0;
	#forming points and grouping them into Quadrants
	points = {}
	points['I']=[]
	points['II']=[]
	points['III']=[]
	points['IV']=[]
	for i in range(0,W):
		for j in range(0,W):
			d =(i-(W/2))*(i-(W/2))+(j-(W/2))*(j-(W/2))
			d= int(sqrt(d))		
			if d<W/2:

				if i-W/2 >0:
					if j-W/2< 0:
						points['I'].append([i,j])
					elif j-W/2 >0:
						points['IV'].append([i,j])
				elif i-W/2<0:
					if j-W/2<0:
						points['II'].append([i,j])
					elif j-W/2>0:
						points['III'].append([i,j])
	return points
	

