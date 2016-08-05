#localization for MULTIPLE languages... kek

promptDivisor = "-"*79

promptFilterList = """Bienvenido a LashImageFilter, seleccione el filtro a realizar
0.- Girar 90 grados
1.- Girar -90 grados
2.- Espejo Horizontal
3.- Espejo Vertical
4.- Intercambiar color (RGB)
5.- Negativo
6.- Blanco y Negro
7.- Todos somos Chile 
8.- Glitch Horizontal
9.- -> Filtros Experimentales
"""

promptImageLoadRoute = "Ingrese ruta al archivo a filtrar: "
promptImageLoadError = "Error al cargar archivo, intente nuevamente."

promptLoadingImage = "Cargando Imagen, porfavor espere..."
promptLoadingSuccess = "Cargado completado."

promptFilterText = "Ingrese Filtro a usar (0..9): "
promptExitText = "Desea realizar otra operacion? (Y/N): "

promptSuccess = "Operacion Exitosa!"

promptShowImage = "Desea abrir la nueva imagen en su visor predeterminado? (Y/N): "

promptInvalidArgument = "Argumento invalido ingresado."
promptNotInteger = "El argumento entregado no es un numero entero (no es transformable a int)"
promptOverLimit = "El argumento entregado sobrepasa el numero de alternativas"

promptChooseChannels = """ Elija el canal de color que desea conservar\n
Los colores se clasifican en RGB, donde R es rojo, G es verde y B es azul.
Listado de posibilidades:
0.- Solo Rojo     (R)
1.- Solo Verde    (G)
2.- Solo Azul     (B)
3.- Rojo y Verde  (RG)
4.- Verde y Azul  (GB)
5.- Rojo y Azul   (RB)
#los valores omitidos se reemplazan con 000 en la escala 0-255
"""

promptChooseInput = "Seleccione un valor de la lista: "

promptChooseLuma = """ Para lograr un efecto B&W perfecto, es necesario usar un factor
llamado Luma, el cual se obtiene con la formula 'Luma = (Red * 0.2126 + Green * 0.7152 + Blue * 0.0722)'
al usar Luma, los colores representan de mejor manera su equivalente en gris que usando el metodo
de sumar los tres componentes y dividir por tres.
Desea utilizar el factor Luma? (Y/N): """

promptAssumedZero = "Error durante seleccion, valor 0 asumido."

promptGlitchModes = """Hay disponibles dos tipos de glitch.
el normal, funciona por segmentos de cantidad aleatoria,
otorgando el mismo desfase horizontal para cada desfase.
mientras que el avanzado, funciona por pixel.
"""
promptGlitchMode = "Desea usar el glitch por pixel? (Y/N): "

promptBlurStrengthHor = "Ingrese la intensidad del desenfoque horizontal (default:4): "
promptBlurStrengthVer = "Ingrese la intensidad del desenfoque vertical   (default:4): "

promptApplyingHorBlur = "Aplicando Blur horizontal..."
promptApplyingVerBlur = "Aplicando Blur vertical..."
promptApplyRadialBlur = "Aplicando Blur radial"