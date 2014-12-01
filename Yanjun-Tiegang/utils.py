from random import randrange
import numpy as np
from math import sqrt

"""



"""
def insideCircle(i,j,radius):
	x,y=radius,radius
	d =sqrt((i-x)*(i-x)+(j-y)*(j-y))
	if d<=radius:
		return True
	else:
		return False
	

def pointsInsideCircle(radius):
	W = radius
	i=0;j=0;
	#forming points and grouping them into Quadrants
	points = {}
	points['I']=[]
	points['II']=[]
	points['III']=[]
	points['IV']=[]
	for i in range(0,2*W):
		for j in range(0,2*W):
			if i < W:
				if j<W:
					if insideCircle(i+1,j+1,W):
						points["II"].append([i,j])
				else:
					if insideCircle(i+1,j,W):
						points["III"].append([i,j])
			else:
				if j<W:
					if insideCircle(i,j+1,W):
						points["I"].append([i,j])
				else:			
					if insideCircle(i,j,W):
						points["IV"].append([i,j])


				"""
					points (x,y) differ from block (i,j) in different quadrants
					for Quadrant I, point(x,y) denotes (x,y-1) block
					for Quadrant II, point(x,y) denotes (x-1,y-1) block
					for Quadrant I, point(x,y) denotes (x-1,y) block
					for Quadrant I, point(x,y) denotes (x,y) block
				"""
	return points
	
def compare(v1,v2,posA,posB,Dsim,Nd):
	sim = sqrt(pow(v1[0]-v2[0],2)+pow(v1[1]-v2[1],2)+pow(v1[2]-v2[2],2)+pow(v1[3]-v2[3],2))
	if sim > Dsim and sim < 0.2:
		d = sqrt(pow(posA[0]-posB[0],2)+pow(posB[0]-posB[1],2))
		if d > Nd:
			print [d,sim]
			return True
		else:
			return False
	else:
		return False

		
def zigzag(max_value):
	coeffs = [[],[],[],[]]
	counter = 0
	index = 0
	for i in range(0,max_value+1):
		j = i
		for k in range(0,i+1):
			if i%2 == 0:
				coeffs[index].append([j,k])
			else:
				coeffs[index].append([k,j])
			j=j-1
			counter = counter+1
			if counter%max_value == 0:
				index = index+1
	coeffs[index].append([0,max_value+1])
	return coeffs
