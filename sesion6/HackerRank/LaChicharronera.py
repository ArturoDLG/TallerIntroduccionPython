def formula_gral(c, b=1, a=1):
    """Funcion para calcular los valores de X de una ecuacion de 2do grado.
	a (X^2) y b(X) por defecto son 1"""
    r= (b**2 - 4*a*c)**(1/2)
    # En una ecuacion de 2do grado X tiene 2 valores
    return (-b+r)/(2*a), (-b-r)/(2*a)

if __name__ == '__main__':
    a, b, c = input().split()
    c = int(c)  # convertimos a int a 'c'
    x1, x2 = 0,0  #  inicalizamos a x1 y a x2 en 0
    if a == '-':
        if b == '-':
            x1, x2 = formula_gral(c)  # usamos los valores por defecto de a y b
        else:
            b = int(b)  # convertimos a int a 'b'
            x1, x2 = formula_gral(c, b)  # usamos el valor por defecto de a
    else:
        a, b = int(a), int(b)  # convertimos a int a 'a' y 'b'
        x1, x2 = formula_gral(c, b, a)
    # Imprimimos los vaores obtenidos de x1 y x2
    print(f'x1={int(x1)}')
    print(f'x2={int(x2)}')
