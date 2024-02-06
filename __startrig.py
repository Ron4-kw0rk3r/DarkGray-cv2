#/usr/bin/python3



import cv2 

import sys
from functools import cache 


@cache 

def _scape(attrib):
	img = cv2.imread( attrib ,cv2.IMREAD_GRAYSCALE)

	print("convirtiendo en escala de grises ...")

	cv2.imshow(attrib,img)

	cv2.imwrite(attrib, img)
_scape(sys.argv[1])