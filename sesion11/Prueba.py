class RGB(object):
    def __init__(self, red, green, blue):
        if not all(self.is_rgb(color) for color in (red, green, blue)):
            raise ValueError('Los colores estan fuera del rango RGB')
        self.__red = red  # Atributo privado
        self.__green = green
        self.__blue = blue

    def is_rgb(self, color):
        return 0 <= color <= 255

    def __repr__(self):
        return f'Color(red={self.__red}, green={self.__green}, blue={self.__blue})'

    @property
    def green(self):
        return self.__green

    @green.setter
    def green(self, value):
        if not self.is_rgb(value):
            raise ValueError('El color esta fuera del rango RGB')
        else:
            self.__green = value


class Punto(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'<{self.x},{self.y}>'

    def __add__(self, other):
        return Punto(self.x + other.x,
                     self.y + other.y)

    def __sub__(self, other):
        return Punto(self.x - other.x,
                     self.y - other.y)