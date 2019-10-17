if __name__ == '__main__':
    refrescos = input().split()
    refresco = input()
    cant = refrescos.count(refresco)
    if cant:
        print('Hay {} botellas del refresco {}'.format(cant, refresco))
    else:
        print('Lo sentimos, producto no disponible')
