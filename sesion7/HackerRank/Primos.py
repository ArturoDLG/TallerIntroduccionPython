from sys import stdin, stdout

def primos(n):
	"""Generador de numeros primos desde 2 a n"""
	def es_primo(numero):
		if numero == 2:
			return True
		if not numero % 2:
			return False

		for divisor in range(3,int(numero**0.5)+1):
			#print('*',divisor)
			if not numero%divisor:
				#print('d')
				return False
		return True
	
	for numero in range(2,n+1):
		#print('-',numero)
		if es_primo(numero):
			yield numero

if __name__ == '__main__':
	n = int(next(stdin))
	for primo in primos(n):
		stdout.write(f'{primo}\n')
