#import all things needed
import os, PIL
from P1_funciones import * #provided image loading function
from LashFilter import * #the filterImage function comes from here, also here are all the functions used for the filters
from Localize import * #every print is a constant variable from Localize (for easy translation... kek)

def loadImage(image):
	#set some variables based on image route and name
	global imageName, imageExtension, imageRoute
	imageRoute = image
	imageName, imageExtension = os.path.splitext(imageRoute)
	print promptLoadingImage
	#load image on PIL and get an array as input for following functions
	testImage = convertirImagenAArchivo(imageRoute, "temp.file")
	testList = leerArchivo("temp.file")
	print promptLoadingSuccess
	
	#return the generated list that represents the original image
	return testList

if __name__ == "__main__":
	def main():
		#try to load the provided image route, if invalid, ask to try again
		try:
			testList = loadImage(raw_input(promptImageLoadRoute))
		except:
			print promptImageLoadError
			return False
		
		#Show list of possible filters
		print "\n",
		print promptFilterList
		
		#get input from user
		usedFilter = raw_input(promptFilterText)
		print "\n"
		
		#use selected filter
		newList = filterImage(usedFilter, testList)
		#output
		newName = imageName+"_"+str(usedFilter)+imageExtension
		convertirMatrizAImagen(newList, newName)
		
		#delete temporary files created during init
		os.remove("temp.file")
	
	#run program
	main()
	while raw_input(promptExitText).lower() in "yes1ok": #user wants to process another image, run again
		print "\n"
		main()
	
	#out of loop, exit program
	os._exit(1)