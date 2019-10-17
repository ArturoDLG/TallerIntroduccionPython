if __name__ == '__main__':
    a, b = input().split()
    a, b = int(a), int(b)
    for i in range(a, b+1):
        print(f'{i} * {i} = {i**2}')
