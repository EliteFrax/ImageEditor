from PIL import Image
import numpy

def convertirImagenAArchivo(nombreImagen, nombreDestino):
	imagen = Image.open(nombreImagen)
	imagen = imagen.convert('RGBA')
	matrizNumpy = numpy.array(imagen)
	archivo = open(nombreDestino, 'w')
	for fila in matrizNumpy:
		for pixel in fila :
			for componente in pixel :
				archivo.write(' ' + str(componente))
			archivo.write(',')
		archivo.write('\n')
	archivo.close()
	return True

def leerArchivo(nombreEntrada):
	archivo = open(nombreEntrada,'r')
	matriz = []
	for i in archivo:
		lista = []
		fila = []
		lista = i.strip(",\n").split(',')
		for pixel in lista :
			aux = pixel.split()
			for e in range(4) :
				aux[e] = int(aux[e])
			fila.append(aux)
		matriz.append(fila)
	return matriz

def convertirMatrizAImagen(matriz, nombreSalida):
	arr = numpy.array(matriz)
	im = Image.fromarray(arr.clip(0,255).astype('uint8'), 'RGBA')
	im.save(nombreSalida)
	return True