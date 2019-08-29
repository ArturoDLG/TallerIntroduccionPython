if __name__ == '__main__':
	r = input()  # Radio del circulo
	"""
	Recordar que input devuelve siempre un str, por lo que se debe de convertir al tipo de dato
	que el problema requiera, en este caso, float es el mas conveniente, ya que los resultados pueden\
	ser de tipo int o float.
	"""
	r = float(r)
	PI = 3.1416  # Valor para PI definido por el problema
	area = PI * r ** 2
	perimetro = PI * r * 2
	# Forma mas correcta de imprimir las salidas solicitadas
	print(f'A: {area}')
	print(f'P: {perimetro}')
	"""
	Otra manera de imprimir la salida sin las f-strings es usando multiples argumentos en
	print:
	print('A:',area)
	print('P:',perimetro)
	Note que no hay espacio despues del ':', ya que print los coloca por default
	"""
