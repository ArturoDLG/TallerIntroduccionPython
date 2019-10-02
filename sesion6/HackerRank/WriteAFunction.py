"""Para este problema se debe de crear una funcion"""
def is_leap(year):
    """Retorna si el año es bisiesto o no"""
    leap = False  # inicializamos la variable en False
    
    if not year % 4:  # si es multiplo de 4
        if not year % 100:  # si es multiplo de 100
            if not year % 400:  # si es multiplo de 400
                leap =  True
        else:
            leap =  True
    
    return leap
