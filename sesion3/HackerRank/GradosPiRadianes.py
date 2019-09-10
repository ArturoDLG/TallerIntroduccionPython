import math

if __name__ == '__main__':
	#  Entrada del problema, para este problema nosotros recibimos un numero float
	#  recordemos que el valor esta en grados
	grados = float(input())
	#  Convertimos los grados a radianes, y dividimos entre pi, para obtener pi radianes
	resultado = math.radians(grados)/math.pi
	print(f'{resultado} pi radianes')
	"""
	Otra manera de mostrar la salida con lo visto en la clase es:
	print(resultado,'pi radianes')
	"""
