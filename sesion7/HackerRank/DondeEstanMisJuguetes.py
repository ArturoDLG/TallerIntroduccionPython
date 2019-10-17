if __name__ == '__main__':
    j = int(input())
    juguetes = set()
    for _ in range(j):
        juguete = input()
        juguetes.add(juguete)
    q = int(input())
    for _ in range(q):
        query = input()
        if query in juguetes:
            print('Si')
        else:
            print('No')
