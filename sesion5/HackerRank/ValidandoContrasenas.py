if __name__ == '__main__':
    password = input()
    if password.isalnum():
        print('La contraseña es valida')
    else:
        print('La contraseña es invalida, vuela a intentarlo')
