import math

if __name__ == '__main__':
	#  Entrada, los datos deben ser de tipo entero para este ejercicio
	a = int(input())
	b = int(input())
	#  Para calcular el maximo comun divisor usamos gcd
	resultado = math.gcd(a, b)
	print(resultado)
