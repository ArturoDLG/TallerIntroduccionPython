from collections import Counter

if __name__ == '__main__':
    n = int(input())
    registradora = Counter(input() for _ in range(n))
    """for _ in range(n):
        producto = input()
        registradora[producto] += 1"""
    k = int(input())
    mas_populares = registradora.most_common(k)
    for p, _ in mas_populares:
        print(p)