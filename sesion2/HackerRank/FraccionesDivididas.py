#  Para este ejercicio es importante usar la clase Fraction del modulo fractions
from fractions import Fraction


if __name__ == '__main__':
	f1 = input()
	f2 = input()
	"""
	Recordar que input devuelve un str, por lo que debe convertirse al tipo de dato necesario.
	Para este caso, debe usarse Fraction del modulo fractions
	"""
	f1 = Fraction(f1)
	f2 = Fraction(f2)
	resultado = f1/f2
	print(resultado.numerator)  # Numerador del resultado
	print(resultado.denominator)  # Denominador del resultado
