def numero_capicua(n):
    """Retorna la cadena 'Si', si el numero es capicua, de caso contrario, devuelve la
	cadena 'No'.
	Un numero capicua es todo numero que sus digitos se pueden escribir igual de 
	izquierda a derecha y visceversa."""
    return 'Si' if n == n[::-1] else 'No'

if __name__ == '__main__':
    N = int(input())  # Leemos el numero de casos
    for _ in range(N):
        número = input()  # Para este problema no es necesario convertir a int el numero
        print(numero_capicua(número))
