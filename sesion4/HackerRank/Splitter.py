
if __name__ == '__main__':
	nombre = input()
	t1 = input()
	t2 = input()
	t3 = input()
	"""
	La manera mas sencilla de concatenar el nombre y las cadenas que forman el
	numero telefonico son las f-strings
	"""
	print(f'{nombre}: {t1}-{t2}-{t3}')
	"""
	Otra alternativa un tanto mas complicada, es el guardar t1, t2 y t3 en una lista
	y concatenarlo con el metodo join de la siguiente manera:
	telefono = '-'.join([t1, t2, t3])
	print(f'{nombre}: {telefono}')
	"""
