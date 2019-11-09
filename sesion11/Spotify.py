from dataclasses import dataclass
from collections import deque
from random import choice

@dataclass
class Cancion(object):
    nombre: str
    artista: str
    album: str
    fecha_publicacion: str

class Playlist(object):
    def __init__(self, nombre_playlist):
        self.nombre = nombre_playlist
        self.__lista = deque()
        self.__en_cola = deque()

    def __str__(self):
        playlist = [f"{i}: {cancion}" for i, cancion in enumerate(self.__lista, 1)]
        cola = [f"{cancion}" for cancion in self.__en_cola]
        return f"Playlist {self.nombre}:\n" + \
               "En cola: \n" + ("\n".join(cola) if cola else '') + "\n" + \
               "\n".join(playlist)

    def agregar(self, cancion):
        """Agregar una cancion a la lista"""
        self.__lista.append(cancion)

    def eliminar(self, posicion):
        """Eliminar una determinada cancion de la lista"""
        self.__lista.pop(posicion)

    def agregar_cola(self, cancion):
        """Agregar una cancion para reproducir enseguida"""
        self.__en_cola.append(cancion)

    def aleatorio(self):
        """Reproducir la playlist en orden aleatorio, si hay canciones en cola,
        estas se repoducen en el orden de inserccion"""
        yield from self.__cola()
        orden = self.__lista.copy()
        for _ in range(len(orden)):
            cancion = choice(orden)
            yield cancion
            orden.remove(cancion)

    def __cola(self):
        while self.__en_cola:
            yield self.__en_cola.popleft()

    def __iter__(self):
        """Reproducir la playlist en orden de inserccion, si hay canciones en cola,
           estas se repoducen en el orden de inserccion"""
        yield from self.__cola()
        for cancion in self.__lista:
            yield cancion