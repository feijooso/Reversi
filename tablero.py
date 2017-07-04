def inicializar_tablero():
    tablero = []

    #Inicializamos el tablero vacio, representamos vacio con guiones
    for i in range(0, 10):
        tablero.append([])

        for j in range(0, 10):
            tablero[i].append('-')

    #Ponemos numeros para las posiciones
    #Filas
    for j in range(0, 10):
        tablero[0][j] = j

    #Columnas
    for i in range(0, 10):
        tablero[i][0] = i

    #Asterisco para el resto de los bordes
    i = 9
    for j in range(0, 10):
        tablero[i][j] = '*'
    j = 9
    for i in range(0, 10):
        tablero[i][j] = '*'

    #Ponemos las fichas iniciales
    tablero[4][4]='X'
    tablero[4][3]='O'
    tablero[3][3]='O'
    tablero[3][4]='O'
    tablero[3][5]='O'
    tablero[4][5]='O'
    tablero[5][5]='O'

    return tablero

def mostrar_tablero(tablero):
    for row in tablero:
        print(*row)

tablero=inicializar_tablero()
mostrar_tablero(tablero)
