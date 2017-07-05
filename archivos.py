
def menu():

    salir=False

    while not salir:
            print('1.Jugar')
            print('2.Cargar, generar o actualizar archivo')
            print('3.Salir')

            opcion = int(input('Ingrese su opcion '))

            if opcion==1:
                juego()

            elif opcion==2:
                print('1.Resetear archivo')
                print('2. Cargar nuevo archivo')
                print('3. Aparear archivos')
                print('4.Generar archivo')
                print('5. Mostrar archivo')

                opcion = int(imput('Ingrese su opcion '))

            elif opcion==3:
                salir=True

            else:
                print('Opcion invalida. Ingrese 1, 2 o 3')
