if __name__ == '__main__':
	titulo = input()	
	"""
	Tenemos 2 maneras de centrar el titulo, para este caso, siempre sera a 
	30 unidades; la primera manera es usando la notacion que ofrece las f-string,
	o podemos usar el metodo center de la clase str
	"""
	#  1er metodo
	print('-'*30)
	print(f'{titulo:^30}')
	#  2do metodo
	#  print(titulo.center(30))
	print('-'*30)
