if __name__ == '__main__':
    n = int(input())
    jugadores = []
    for _ in range(n):
        nombre, equipo, goles = input().split()
        equipo = int(equipo)
        goles = int(goles)
        jugadores.append((goles, -equipo, nombre))
    mejor_jugador = max(jugadores)
    print(mejor_jugador[2])
