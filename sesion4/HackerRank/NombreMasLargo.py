if __name__ == '__main__':
	nombres = input().split()
	"""
	Nosotros podemos tener 3 variables y usar asignacion multiple:
	n1, n2, n3 = input().split()

	split() separa por default por espacios en blanco
	"""
	#  Utilizamos el argumento key, para emplear len y nos devuelva las longitudes
	#  de las cadenas
	nombre_mas_largo = max(nombres, key=len)
	print(nombre_mas_largo)

