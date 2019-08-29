if __name__ == '__main__':
	b = input()  # base del numero
	n = input()  # numero a pasar de la base b a decimal
	"""
	Recordar que input nos devuelve un str, por lo que debe convertirse al tipo de dato necesario.
	En este caso, solo b sera necesario transformar a int, ya que n necesita ser un str.
	"""
	b = int(b)
	resultado = int(n, base=b)  # conversion de b a 10
	print(resultado)
