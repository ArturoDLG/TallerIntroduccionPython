from collections import defaultdict

if __name__ == '__main__':
	n = int(input())
	mapa = defaultdict(list)
	for _ in range(n):
		origen, destino = input().split()
		mapa[origen].append(destino)
		mapa[destino].append(origen)
	q = int(input())
	for _ in range(q):
		ciudad = input()
		vecinos = mapa[ciudad]
		for v in vecinos:
			print(v, end=' ')
		print()