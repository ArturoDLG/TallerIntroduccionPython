import math

if __name__ == '__main__':
	#  Entradas del programa, X y Y para este problema son de tipo int
	x = int(input())
	y = int(input())
	#  Debemos de calcular la hipotenusa formada con la cuerda con hypot
	resultado = round(math.hypot(x,y),3)
	print(resultado)
