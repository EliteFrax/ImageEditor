#LashFilters
#libreria para filtros basicos
#destinado para tarea de Introduccion
#a la ingenieria. UTFSM

#Jorge Botarro
#Jose Contreras
#Francisco Bricenio

import math, numpy, random
from copy import deepcopy
from Localize import *

def point_distance(x1,y1,x2,y2):
	return math.hypot(x2-x1, y2-y1)


#this function creates an empty CxR matrix, variable order is WIDTH x HEIGHT
#but return order is HEIGHT x WIDTH to match conventions
#matrixExample[Y][X] = DATA
def createZeroMatrix(Row=2, Col=2):
	tempMatrix = []
	f = Row
	c = Col
	
	for y in range(f):
		tempMatrix.append([])
		for x in range(c):
			tempMatrix[y].append(0)
			
	return tempMatrix

#RowxCol matrix filled with [255,255,255,255] tuples
def createWhiteMatrix(Row=2, Col=2):
	tempMatrix = []
	f = Row
	c = Col
	
	for y in range(f):
		tempMatrix.append([])
		for x in range(c):
			tempMatrix[y].append([0,0,0,0])
			
	return tempMatrix
	
#Transpose the matrix to get the "flipped" version
#Example:
# 1|2    
# 3|4 => 1|3|5
# 5|6    2|4|6
def transposeMatrix(matrix):
	#get matrix dimensions
	f = len(matrix)
	if type(matrix[0]) == int:
		c = 1
	else:
		c = len(matrix[0])
	
	#create "transposed" empty matrix
	tempMatrix = createZeroMatrix(c,f)
	
	#iterate matrix and get values
	for C in range(c): #Y
		for F in range(f): #X
			tempMatrix[C][F] = matrix[F][C]

	return tempMatrix

#horizontal flip
def hMirrorMatrix(matrix):
	f = len(matrix)
	#create copy of array
	if type(matrix[0]) == int:
		c = 1
	else:
		c = len(matrix[0])
	tempMatrix = createZeroMatrix(f,c)
	for y in range(f):
		tempMatrix[y] = matrix[y][::-1]
	
	return tempMatrix
	
#vertical flip
def vMirrorMatrix(matrix):
	f = len(matrix)
	#test if len(height) == 1 and return unmodified
	if f <= 1: return matrix
	#else get variables
	c = len(matrix[0])
	#loop matrix and flip y axis
	tempMatrix = createZeroMatrix(f,c)
	for y in range(f):
		for x in range(c):
			tempMatrix[y][x] = matrix[f-(y+1)][x]
			
	return tempMatrix
	
#90 degrees rotation is a transpose with horizontal flip
#and -90 degrees rotation is a transpose with vertical flip
#not the fastest way to do, and wastes memory like crazy, but works
#for ~1920x1080 images with no problem in my pc
def rotateMatrix(matrix, isLeft = 0):
	transposedMatrix = transposeMatrix(matrix)
	if isLeft:
		return vMirrorMatrix(transposedMatrix)
	else:
		return hMirrorMatrix(transposedMatrix)

#explicit, takes the color, and subtract color to 255
#formula: color = [255-r, 255-g, 255-b, a]
def invertColors(matrix):
	f = len(matrix)
	c = len(matrix[0])
	tempMatrix = createWhiteMatrix(f,c)
	
	for y in range(f):
		for x in range(c):
			tempMatrix[y][x] = [255 - matrix[y][x][0], 255 - matrix[y][x][1], 255 - matrix[y][x][2], matrix[y][x][3]] #'cos alpha channel
			
	return tempMatrix
	
#sets unchecked color channels to 0 and keeps checked values
def keepChannel(matrix, channel = 0):
	f = len(matrix)
	if type(matrix[0]) == int:
		c = 1
	else:
		c = len(matrix[0])
	tempMatrix = createWhiteMatrix(f,c)
	try:
		channel = int(channel)
	except:
		print promptInvalidArgument
		return matrix
	#channel list
	# 0 = r only
	# 1 = g only
	# 2 = b only
	# 3 = r + g
	# 4 = g + b
	# 5 = r + b
	
	r = (channel == 0 or channel == 3                 or channel == 5)
	g = (channel == 1 or channel == 3 or channel == 4                )
	b = (channel == 2                 or channel == 4 or channel == 5)
	
	for y in range(f):
		for x in range(c):
			tempMatrix[y][x] = [r*matrix[y][x][0], g*matrix[y][x][1], b*matrix[y][x][2], matrix[y][x][3]] #keep alpha channel the same
			
	return tempMatrix
		
# general formula: val = (r + g + b) / 3; color = [val, val, val, a]
# luma formula: color = ((r * 0.2126) + (g * 0.7152) + (b * 0.0722))
def blackAndWhite(matrix, luma = 0):
	f = len(matrix)
	if type(matrix[0]) == int:
		c = 1
	else:
		c = len(matrix[0])
	tempMatrix = createWhiteMatrix(f,c)
	val = 0
	
	for y in range(f):
		for x in range(c):
			if luma in "yes1ok":
				val = (matrix[y][x][0] * 0.2126
				     + matrix[y][x][1] * 0.7152
					 + matrix[y][x][2] * 0.0722)
			else:
				val = (sum(matrix[y][x][0:4])/3)
			tempMatrix[y][x] = [val,val,val,matrix[y][x][0]]
			
	return tempMatrix
		
#blends 50% blue per pixel if y < (50% of H) and x < (50% of W),
#blends 50% white per pixel if y < (50% of H) and x > (50% of W),
#or blends 50% red if y > (50% of H)
def chileanPride(matrix):
	f = len(matrix)
	if type(matrix[0]) == int:
		c = 1
	else:
		c = len(matrix[0])
	tempMatrix = createWhiteMatrix(f,c)
	color = [0,0,0,255] #create a blank color variable
	
	upper = 0
	
	for y in range(f):
		inRed = (y > (f/2))
		for x in range(c):
			if inRed:
				color = [255,0,0] #red
			else:
				if (x < c/2):
					color = [0,0,255] #blue
				else:
					color = [255,255,255] #white
			
			tempMatrix[y][x] = [(matrix[y][x][0] + color[0])/2, (matrix[y][x][1] + color[1])/2, (matrix[y][x][2] + color[2])/2, matrix[y][x][3]]
	
	return tempMatrix
	
#gets the k offset from a random generated list of offsets
#and applies this offset based on position relative to H.
#snaps the image along the x axis by OFFSET[k] pixels.
#if snapped location is > W or is < 0, wrap along x axis
def glitchMe(matrix):
	f = len(matrix)
	if type(matrix[0]) == int:
		c = 1
	else:
		c = len(matrix[0])
	tempMatrix = createWhiteMatrix(f,c)
	
	offset = []
	chunks = random.randint(3,7)
	for i in range(chunks):
		offset.append(random.randint(-c/3, c/3))
		
	for y in range(f):
		actualY = int(math.floor((y/float(f))*chunks))
		for x in range(c):
			actualX = (x + offset[actualY]) % c
			tempMatrix[y][x] = matrix[y][actualX]
			
	return tempMatrix

#the same as glitchMe(image), but uses a random offset
#for every row of the image, is way less strong, but gives
#a blurry efect
def ultraGlitch(matrix):
	f = len(matrix)
	if type(matrix[0]) == int:
		c = 1
	else:
		c = len(matrix[0])
	
	tempMatrix = createWhiteMatrix(f, c)
	
	for y in range(f):
		offset = random.randint(-(c/40), (c/40))
		for x in range(c):
			actualX = (x + offset) % c
			tempMatrix[y][x] = matrix[y][actualX]
	
	return tempMatrix
	
#1D horizontal Box blur pass, with variable radii
def horBoxBlur(matrix, radii = 2):
	f = len(matrix)
	if type(matrix[0]) == int:
		c = 1
	else:
		c = len(matrix[0])
	tempMatrix = createWhiteMatrix(f,c)
	rr = (2*radii)+1
	
	for y in range(f):
		for x in range(c):
			value = [0,0,0,0]
			for i in range(rr):
				j = min(max((x - radii + i), 0), c-1)
				value = [value[0] + matrix[y][j][0],
				         value[1] + matrix[y][j][1],
						 value[2] + matrix[y][j][2],
						 value[3] + matrix[y][j][3]]
			value = [value[0]/rr, value[1]/rr, value[2]/rr, value[3]/rr]
			tempMatrix[y][x] = value
	
	return tempMatrix
	
#1D vertical Box blur pass, with variable radii	
def verBoxBlur(matrix, radii = 2):
	f = len(matrix)
	if type(matrix[0]) == int:
		c = 1
	else:
		c = len(matrix[0])
	tempMatrix = createWhiteMatrix(f,c)
	rr = (2*radii)+1
			
	for y in range(f):
		for x in range(c):
			value = [0,0,0,0]
			for i in range(rr):
				j = min(max((y - radii + i), 0), f-1)
				value = [value[0] + matrix[j][x][0],
				         value[1] + matrix[j][x][1],
						 value[2] + matrix[j][x][2],
						 value[3] + matrix[j][x][3]]
			value = [value[0]/rr, value[1]/rr, value[2]/rr, value[3]/rr]
			tempMatrix[y][x] = value
			
	return tempMatrix
			
def radialBlend(matrix, radii_h = 4, radii_v = 4):
	f = len(matrix)
	if type(matrix[0]) == int:
		c = 1
	else:
		c = len(matrix[0])
	tempBlurred = createWhiteMatrix(f,c)
	tempMatrix = createWhiteMatrix(f,c)
	
	print promptApplyingHorBlur
	tempBlurred = horBoxBlur(matrix, radii_h)
	print promptApplyingVerBlur
	tempBlurred = verBoxBlur(tempBlurred, radii_v)
	
	#apply blend between blurred and normal based on distance
	print promptApplyRadialBlur
	dc = point_distance(0, 0, (f-1)/2.0, (c-1)/2.0)
	for y in range(f):
		for x in range(c):
			dd = point_distance(x, y, (f-1)/2.0, (c-1)/2.0)
			d = min( ((3.0*dd) / (dc)), 1.0)
			#print d, 1.0-d, d + (1.0-d)
			v1 = ( (d*tempBlurred[y][x][0]) + ((1.0-d)*matrix[y][x][0]) )
			v2 = ( (d*tempBlurred[y][x][1]) + ((1.0-d)*matrix[y][x][1]) )
			v3 = ( (d*tempBlurred[y][x][2]) + ((1.0-d)*matrix[y][x][2]) )
			v4 = ( (d*tempBlurred[y][x][3]) + ((1.0-d)*matrix[y][x][3]) )
			
			tempMatrix[y][x] = map(int, [v1, v2, v3, v4])
	
	return tempMatrix
			
#based on the input filter (0-1x), performs the assigned filter
# to the matrix and returns the modified version.
def filterImage(filter, image):
	if filter == "0" or filter == "rotate90r": #rotate 90 degrees
		image = rotateMatrix(image, 0)
		
	elif filter == "1" or filter == "rotate90l": #rotate 90 degrees, counter-clockwise
		image = rotateMatrix(image, 1)	
		
	elif filter == "2" or filter == "horflip": #horizontal flip
		image = hMirrorMatrix(image)
	
	elif filter == "3" or filter == "verflip": #vertical flip
		image = vMirrorMatrix(image)
	
	elif filter == "4" or filter == "keepchannel": #keep channel
		print promptChooseChannels
		keepedChannel = raw_input(promptChooseInput)
		try:
			keepedChannel = int(keepedChannel)
			if keepedChannel > 5:
				print promptOverLimit
				return image
		except:
			print promptNotInteger
			return image
		image = keepChannel(image, keepedChannel)
	
	elif filter == "5" or filter == "invert": #invert color
		image = invertColors(image)
		
	elif filter == "6" or filter == "bnw": #black and white
		print promptChooseLuma,
		luma = raw_input("")
		image = blackAndWhite(image, luma)
		
	elif filter == "7" or filter == "chile": #'todos somos chile'
		image = chileanPride(image)
		
	elif filter == "8" or filter == "glitch": #glitch
		print promptGlitchModes
		selected = raw_input(promptGlitchMode)
		if selected in "yes1ok":
			image = ultraGlitch(image)
		else:
			image = glitchMe(image)
		
	elif filter == "boxhor": #horizontal one pass blur
		radii = raw_input(promptBlurStrengthHor)
		try:
			radii = int(radii)
		except:
			radii = 4
		
		print promptApplyingHorBlur
		image = horBoxBlur(image, radii)
		
	elif filter == "boxver": #vertical one pass blur
		radii = raw_input(promptBlurStrengthVer)
		try:
			radii = int(radii)
		except:
			radii = 4

		print promptApplyingVerBlur
		image = verBoxBlur(image, radii)
		
	elif filter == "box2d": #2d one pass blur
		radii_h = raw_input(promptBlurStrengthHor)
		radii_v = raw_input(promptBlurStrengthVer)
		try:
			radii_h = int(radii_h)
		except:
			radii_h = 4
		try:
			radii_v = int(radii_v)
		except:
			radii_v = 4

		print promptApplyingHorBlur
		image = horBoxBlur(image, radii_h)
		print promptApplyingVerBlur
		image = verBoxBlur(image, radii_v)
		
	elif filter == "boxrad": #radial blur
		radii_h = raw_input(promptBlurStrengthHor)
		radii_v = raw_input(promptBlurStrengthVer)
		try:
			radii_h = int(radii_h)
		except:
			radii_h = 4
		try:
			radii_v = int(radii_v)
		except:
			radii_v = 4

		image = radialBlend(image, radii_h, radii_v)
		
	else:
		return image
	
	#assume success (otherwise early return 0) and return transformed image
	print "\n",
	print promptSuccess
	return image