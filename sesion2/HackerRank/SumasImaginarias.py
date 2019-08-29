if __name__ == '__main__':
	a = input()
	b = input()
	"""
	Recordar que input devuelve un str, y este debe ser convertido a el tipo de dato requerido.
	para este caso se debe convertir en complex
	"""
	a = complex(a)
	b = complex(b)
	resultado = a + b
	print(resultado)
