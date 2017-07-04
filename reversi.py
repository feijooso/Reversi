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
    i = 4
    j = 5
    tablero[i][i] = 'O'
    tablero[j][j] = 'O'
    tablero[i][j] = 'X'
    tablero[j][i] = 'X'

    return tablero

def mostrar_tablero(tablero):
    for row in tablero:
        print(*row)



def pedir_datos_jugador():
    seguir = True

    while seguir:
        jugador = input("Ingrese su nombre: ")

        if len(jugador) >= 4 and len(jugador) <= 8:
            seguir = False
        else:
            print("Su nombre tiene que ser de 4 a 8 caracteres")

    seguir = True

    while seguir:
        ficha = input("Ingrese su ficha (X / O): ")

        if ficha == 'X':
            seguir = False
        elif ficha == 'O':
            seguir = False

    return ficha, jugador


def inicializar_jugador_pc(ficha_jugador):

    if ficha_jugador == 'X':
        ficha_pc = 'O'
    else:
        ficha_pc = 'X'

    return ficha_pc

def tablero_completo(tablero):

    tablero_completo = True
    i = 1

    while tablero_completo and i<9:
        j = 1
        while tablero_completo and j<9:
            if tablero[i][j] == '-':
                tablero_completo = False
            j+=1
        i+=1

    return tablero_completo

def jugadores_tienen_fichas(tablero):

    i = 1
    cantidad_O = 0

    while i<9 and cantidad_O==0:
        j = 1
        while j<9 and cantidad_O==0:
            if tablero[i][j] == 'O':
                cantidad_O+=1
            j+=1
        i+=1

    i = 1
    cantidad_X = 0

    while i<9 and cantidad_X==0:
        j = 1
        while j<9 and cantidad_X==0:
            if tablero[i][j] == 'X':
                cantidad_X+=1
            j+=1
        i+=1

    if cantidad_X>0 and cantidad_O>0:
        return True
    else:
        return False

def coordenada_valida(coordenada):
    if 0<coordenada<10:
        return True
    else:
        return False

def buscar_alrededor(tablero,coordenada_x,coordenada_y,ficha_propia,i,j):
    coordenada_x+=i
    coordenada_y+=j
    posibles_reemplazos = []

    if ficha_propia=='X':
        ficha_rival='O'
    else:
        ficha_rival='X'

    continuar=True

    while coordenada_x>0 and coordenada_x<9 and coordenada_y>0 and coordenada_y<9 and continuar:
        if tablero[coordenada_x][coordenada_y]==ficha_rival:
            posibles_reemplazos.append([coordenada_x,coordenada_y])
        elif tablero[coordenada_x][coordenada_y]==ficha_propia:
            continuar = False
        elif tablero[coordenada_x][coordenada_y]=='-':
            continuar = False
            posibles_reemplazos = []

        coordenada_x+=i
        coordenada_y+=j

    if len(posibles_reemplazos)==0:
        return False, posibles_reemplazos
    else:
        return True, posibles_reemplazos


def puede_reemplazar(tablero,coordenada_x,coordenada_y,ficha):
    jugable_norte, _ = buscar_alrededor(tablero,coordenada_x,coordenada_y,ficha,-1,0)
    jugable_sur, _ = buscar_alrededor(tablero,coordenada_x,coordenada_y,ficha,1,0)
    jugable_este, _ = buscar_alrededor(tablero,coordenada_x,coordenada_y,ficha,0,1)
    jugable_oeste, _ = buscar_alrededor(tablero,coordenada_x,coordenada_y,ficha,0,-1)
    jugable_noreste, _ = buscar_alrededor(tablero,coordenada_x,coordenada_y,ficha,-1,1)
    jugable_noroeste, _ = buscar_alrededor(tablero,coordenada_x,coordenada_y,ficha,-1,-1)
    jugable_sureste, _ = buscar_alrededor(tablero,coordenada_x,coordenada_y,ficha,1,1)
    jugable_suroeste, _ = buscar_alrededor(tablero,coordenada_x,coordenada_y,ficha,1,-1)

    return jugable_norte or jugable_sur or jugable_suroeste or jugable_sureste or jugable_noroeste or jugable_noreste or jugable_este or jugable_oeste

def jugadas_posibles(tablero,coordenada_x,coordenada_y,ficha):
    jugadas_posibles = []

    _ , reemplazos_norte = buscar_alrededor(tablero,coordenada_x,coordenada_y,ficha,-1,0)
    _ , reemplazos_sur = buscar_alrededor(tablero,coordenada_x,coordenada_y,ficha,1,0)
    _ , reemplazos_este = buscar_alrededor(tablero,coordenada_x,coordenada_y,ficha,0,1)
    _ , reemplazos_oeste = buscar_alrededor(tablero,coordenada_x,coordenada_y,ficha,0,-1)
    _ , reemplazos_noreste = buscar_alrededor(tablero,coordenada_x,coordenada_y,ficha,-1,1)
    _ , reemplazos_noroeste = buscar_alrededor(tablero,coordenada_x,coordenada_y,ficha,-1,-1)
    _ , reemplazos_sureste = buscar_alrededor(tablero,coordenada_x,coordenada_y,ficha,1,1)
    _ , reemplazos_suroeste = buscar_alrededor(tablero,coordenada_x,coordenada_y,ficha,1,-1)

    if len(reemplazos_norte)>0:
        for i in range(1,len(reemplazos_norte)+1):
            jugadas_posibles.append(reemplazos_norte[i-1])

    if len(reemplazos_sur)>0:
        for i in range(1,len(reemplazos_sur)+1):
            jugadas_posibles.append(reemplazos_sur[i-1])

    if len(reemplazos_este)>0:
        for i in range(1,len(reemplazos_este)+1):
            jugadas_posibles.append(reemplazos_este[i-1])

    if len(reemplazos_oeste)>0:
        for i in range(1,len(reemplazos_oeste)+1):
            jugadas_posibles.append(reemplazos_oeste[i-1])

    if len(reemplazos_noreste)>0:
        for i in range(1,len(reemplazos_noreste)+1):
            jugadas_posibles.append(reemplazos_noreste[i-1])

    if len(reemplazos_noroeste)>0:
        for i in range(1,len(reemplazos_noroeste)+1):
            jugadas_posibles.append(reemplazos_noroeste[i-1])

    if len(reemplazos_sureste)>0:
        for i in range(1,len(reemplazos_sureste)+1):
            jugadas_posibles.append(reemplazos_sureste[i-1])

    if len(reemplazos_suroeste)>0:
        for i in range(1,len(reemplazos_suroeste)+1):
            jugadas_posibles.append(reemplazos_suroeste[i-1])

    print('jugadas posibles:',jugadas_posibles)

    return jugadas_posibles


def jugada_valida(tablero,ficha,coordenada_x,coordenada_y):

    if tablero[coordenada_x][coordenada_y]=='-':
        if puede_reemplazar(tablero,coordenada_x,coordenada_y,ficha):
            return True

def voltear_fichas(reemplazos,tablero,ficha):

    for i in range (1,len(reemplazos)+1):
        #print("puto", reemplazos)
        tablero[reemplazos[i-1][0]][reemplazos[i-1][1]] = ficha

    return tablero

def juega_usuario(tablero,ficha):
    mostrar_tablero(tablero)
    coordenadas_validas = False

    while not coordenadas_validas:
        coordenada_x = int(input('Ingrese coordenada x: '))
        coordenada_y = int(input('Ingrese coordenada y: '))

        coordenadas_validas = coordenada_valida(coordenada_x) and coordenada_valida(coordenada_y) and jugada_valida(tablero,ficha,coordenada_x,coordenada_y)

    reemplazos = jugadas_posibles(tablero,coordenada_x,coordenada_y,ficha)

    if len(reemplazos)>0:
        tablero[coordenada_x][coordenada_y]=ficha

    tablero = voltear_fichas(reemplazos,tablero,ficha)

    return tablero

def juega_pc(tablero,ficha):
    mostrar_tablero(tablero)
    fichas_reemplazadas= 0
    mejor_jugada = []

    for i in range (1,9):
        for j in range (1,9):
            if jugada_valida(tablero,ficha,i,j):
                reemplazos = jugadas_posibles(tablero,i,j,ficha)
                if len(reemplazos)>fichas_reemplazadas:
                    fichas_reemplazadas = len(reemplazos)
                    coordenadas = [i,j]
                    mejor_jugada = reemplazos

    tablero[coordenadas[0]][coordenadas[1]]=ficha

    tablero=voltear_fichas(mejor_jugada,tablero,ficha)

    return tablero

def turno_X(tablero,ficha_pc,ficha_jugador):

    if ficha_jugador=='X':
        juega_usuario(tablero,ficha_jugador)
    else:
        juega_pc(tablero,ficha_pc)

    return tablero

def turno_O(tablero,ficha_pc,ficha_jugador):

    if ficha_jugador=='O':
        juega_usuario(tablero,ficha_jugador)
    else:
        juega_pc(tablero,ficha_pc)

    return tablero

def jugar(tablero,ficha_pc,ficha_jugador):

    while not tablero_completo(tablero) and jugadores_tienen_fichas(tablero):
        tablero = turno_X(tablero, ficha_pc, ficha_jugador)
        print ('turno x terminado')
        tablero = turno_O(tablero, ficha_pc, ficha_jugador)
        print('turno O terminado')




def main():
    tablero = inicializar_tablero()
    ficha_jugador, jugador = pedir_datos_jugador()
    ficha_pc = inicializar_jugador_pc(ficha_jugador)
    jugar(tablero,ficha_pc,ficha_jugador)


main()
