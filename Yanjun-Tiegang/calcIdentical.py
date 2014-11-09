from cv2 import absdiff
from math import sqrt,pow
def calcIdentical(vector1,vector2,Dsim,Nd):

	m_match = pow(vector1[0]-vector2[0],2) + pow(vector1[1]-vector2[1],2)+ pow(vector1[2]-vector2[2],2)+ pow(vector1[3]-vector2[3],2)
#	print m_match
	m_match = sqrt(m_match)	
	if m_match < Dsim:
#		print m_match
		return True
	else:
		return False
