import csv
def preguntar_nombre():
    seguir = True
 
    while seguir:
        jugador = raw_input("Ingrese su nombre ")
 
        if len(jugador) >= 4 and len(jugador) <= 8:
            seguir = False
        else:
            print("Su nombre tiene que ser de 4 a 8 caracteres")
 
    return jugador

def asignar_fichas():
    repetir = True
    ficha_pc = ""
 
    while repetir:
        ficha_jugador = raw_input('Desea jugar con O o con X? ')
        if ficha_jugador == 'X':
            ficha_pc = 'O'
            repetir = False
        elif ficha_jugador == 'O':
            ficha_pc = 'X'
            repetir = False
        else:
            print('Por favor, ingrese una ficha valida (en mayuscula)')
 
    return ficha_jugador, ficha_pc

def inicializar_matriz_1(tablero):  # guiones
	for i in range(1, 9):
		for j in range(1, 9):
			tablero[i][j] = '-'
	return tablero          
 
def inicializar_matriz_2_1(tablero):  # numeros para las filas
	for j in range(0, 10):
		tablero[0][j] = j + 1
 	return tablero
 
def inicializar_matriz_2_2(tablero):  # numeros para las columnas
	for i in range(0, 10):
		tablero[i][0] = i + 1
	return tablero
 
def inicializar_matriz_2_3(tablero):  # astericos para el resto de los bordes
	i = 9
	for j in range(0, 10):
		tablero[i][j] = '*'
	j = 9
	for i in range(0, 10):
		tablero[i][j] = '*'
	return tablero
 
def inicializar_matriz_3(tablero):
	i = 4
	j = 5
	tablero[i][i] = 'O'
	tablero[j][j] = 'O'
	tablero[i][j] = 'X'
	tablero[j][i] = 'X'
	return tablero

def inicializar_matriz():
	tablero=[]
	for i in range(0, 10):
		tablero.append([])
		for j in range(0, 10):
			tablero[i].append(None)

	tablero=inicializar_matriz_1(tablero)
	tablero=inicializar_matriz_2_3(tablero)
	tablero=inicializar_matriz_2_1(tablero)
	tablero=inicializar_matriz_2_2(tablero)
	tablero=inicializar_matriz_3(tablero)
	return tablero
 
def resetear_tablero(tablero, tablerocom):
	for i in range(0, 10):
		for j in range(0, 10):
			tablerocom[i][j] == tablero[i][j]
 

def mostrar_tablero(tablero):
	for row in tablero:
		for item in row:
			print '{:4}'.format(item),
	print


def tiene_fichas(tablero):
	i=1
	tieneficha=False
	while i<=9 and not tieneficha:
		j=1
		while j<=9 and not tieneficha:
			if tablero[i][j]!='-':
				tieneficha=True
			else:
				j+=1
			i+=1
	return tieneficha

def verificar_tablero_completo(tablero): 
	if tiene_fichas(tablero):
		tablero_completo=False
	else:
		tablero_completo=True
	return tablero_completo


def verificar_coordenadas_validas(i,j,tablero):
	if (i>=1) and (i<=9) and (j>=1) and (j<=9): 
		if tablero[i][j]=='-':
			reintentar=False
		else:
			reintentar=True
	else:
		reintentar=True
	return reintentar

"""def introducir_jugada(tablero):
	vCoords=[0,0]
	reintentar=True
	while reintentar:
		i=input('Introduzca el numero de casilla vertical')
		j=input('Introduzca el numero de casilla horizontal')
		x=int(i)
		y=int(j)
		reintentar=verificar_coordenadas_validas(i,j,tablero)
	vCoords[0]=x
	vCoords[1]=y
	return vCoords"""

def suma_fichas(tablero,ficha):
	fichas=0
	for i in range(0,9):
		for j in range(0,9):
			if tablero[i][j]==ficha:
				fichas+=1
	return fichas

def contar_puntos(tablero,ficha1,ficha2,PJ,PG,PP,PE):
	puntos=suma_fichas(tablero,ficha1)-suma_fichas(tablero,ficha2) 
	PJ+=1
	if suma_fichas(tablero,ficha1)>suma_fichas(tablero,ficha2):
		print ('Ganaste')
		PG+=1
	elif suma_fichas(tablero,ficha1)<suma_fichas(tablero,ficha2):
		print ('Perdiste')
		PP+=1
	elif suma_fichas(tablero,ficha1)==suma_fichas(tablero,ficha2):
		print ('Empate')
		PE+=1
	return puntos,PJ,PG,PP,PE

def seguir_jugando():
	reintentar=True
	while reintentar:
		seguir=raw_input('Desea seguir jugando? S/N')
		if seguir=='S':
			reintentar=False
			return True
		elif seguir=='N':
			reintentar=False
			return False
		else: 
			print "Opcion incorrecta"
		

def fin_juego(tablero,seguir,ficha1,ficha2):
	#aca habria que cargar a puntaje,PJ,PG,PP,PE los datos del usuario para ir sumandolos
	puntos,PJ,PG,PP,PE=contar_puntos(tablero,ficha1,ficha2,usuario,PJ,PG,PP,PE)
	puntaje+=puntos #el puntaje total de todas las partidas que jugo
	seguir=seguir_jugando()
	return seguir,puntos,puntaje,PJ,PG,PP,PE

def verificar_casillero_vacio(tablero,vCoords):
	if tablero[vCoords[0],vCoords[1]]=='-':
		return True
	else:
		return False

def comer_fichas(tablero,tablerocom,vCoords):
	for i in range(0,10):
		for j in range(0,10):
			print tablerocom[i][j]
			if tablerocom[int(i)][int(j)]!='-':
				tablero[i][j]=tablerocom[i][j]
	return tablero

#--- comienzo de los checks

def busca(tablero,vCoords,encontrado,tablerocom,turno,x,y):
	i=vCoords[0]
	j=vCoords[1]
	tablerocom[i][j]=turno
	continuardir=True
	i+=x
	j+=y
	fichascomidas=0
	if turno=='X':
		ficha2='O'
	else:
		ficha2='X'
	while (j>=1) and (j<=9) and (i>=1) and (i<=9) and (continuardir==True):
		if tablero[i][j]==ficha2:
			tablerocom[i][j]=turno
			fichascomidas+=1
			encontrado=True
		elif tablero[i][j]==turno:
			continuardir=False
		elif tablero[i][j]=='-':
			continuardir=False
			tablerocom=resetear_tablero(tablero,tablerocom)
		j+=y
		i+=x
	return fichascomidas,encontrado,tablerocom

def busca_norte(tablero,vCoords,encontrado,tablerocom,turno):
	fichascomidas,encontrado,tablerocom=busca(tablero,vCoords,encontrado,tablerocom,turno,-1,0)
	return fichascomidas,encontrado,tablerocom

def busca_sur(tablero,vCoords,encontrado,tablerocom,turno):
	fichascomidas,encontrado,tablerocom=busca(tablero,vCoords,encontrado,tablerocom,turno,1,0)
	return fichascomidas,encontrado,tablerocom

def busca_este(tablero,vCoords,encontrado,tablerocom,turno):
	fichascomidas,encontrado,tablerocom=busca(tablero,vCoords,encontrado,tablerocom,turno,0,1)
	return fichascomidas,encontrado,tablerocom

def busca_oeste(tablero,vCoords,encontrado,tablerocom,turno):
	fichascomidas,encontrado,tablerocom=busca(tablero,vCoords,encontrado,tablerocom,turno,0,-1)
	return fichascomidas,encontrado,tablerocom

def busca_noreste(tablero,vCoords,encontrado,tablerocom,turno):
	fichascomidas,encontrado,tablerocom=busca(tablero,vCoords,encontrado,tablerocom,turno,-1,1)
	return fichascomidas,encontrado,tablerocom

def busca_noroeste(tablero,vCoords,encontrado,tablerocom,turno):
	fichascomidas,encontrado,tablerocom=busca(tablero,vCoords,encontrado,tablerocom,turno,-1,-1)
	return fichascomidas,encontrado,tablerocom

def busca_sureste(tablero,vCoords,encontrado,tablerocom,turno):
	fichascomidas,encontrado,tablerocom=busca(tablero,vCoords,encontrado,tablerocom,turno,1,1)
	return fichascomidas,encontrado,tablerocom

def busca_suroeste(tablero,vCoords,encontrado,tablerocom,turno):
	fichascomidas,encontrado,tablerocom=busca(tablero,vCoords,encontrado,tablerocom,turno,1,-1)
	return fichascomidas,encontrado,tablerocom

#--- fin de checks


def buscar_prop(tablero,turno,i,j,x,y):
	while (i>=1) and (i<=9) and (j>=1) and (j<=9):
		if tablero[i][j]==turno:
			jugable=True
		i+=x
		j+=y
	return jugable

#_ _ _ checks adyacentes


def buscar_ady(tablero,turno,i,j,x,y,adyencontrado,jugable):
	if adyencontrado and jugable:
		return adyencontrado,jugable
	else:
		terminado=False
		adyencontrado=False
		while not adyencontrado and not terminado:
			i+=x
			j+=y
			if turno=='X':
				ficha2='O'
			else:
				ficha2='X'
			if tablero[i][j]==ficha2:
				adyencontrado=True
				terminado=True
				jugable=buscar_prop(tablero,turno,i,j,x,y)
			else:
				adyencontrado=False
				terminado=True
				jugable=False
			return adyencontrado,jugable

def buscar_ady_norte(tablero,turno,i,j,adyencontrado,jugable):
	adyencontrado,jugable=buscar_ady(tablero,turno,i,j,-1,0,adyencontrado,jugable)
	return adyencontrado,jugable

def buscar_ady_noreste(tablero,turno,i,j,adyencontrado,jugable):
	adyencontrado,jugable=buscar_ady(tablero,turno,i,j,-1,1,adyencontrado,jugable)
	return adyencontrado,jugable

def buscar_ady_este(tablero,turno,i,j,adyencontrado,jugable):
	adyencontrado,jugable=buscar_ady(tablero,turno,i,j,0,1,adyencontrado,jugable)
	return adyencontrado,jugable

def buscar_ady_sureste(tablero,turno,i,j,adyencontrado,jugable):
	adyencontrado,jugable=buscar_ady(tablero,turno,i,j,1,1,adyencontrado,jugable)
	return adyencontrado,jugable

def buscar_ady_sur(tablero,turno,i,j,adyencontrado,jugable):
	adyencontrado,jugable=buscar_ady(tablero,turno,i,j,1,0,adyencontrado,jugable)
	return adyencontrado,jugable

def buscar_ady_suroeste(tablero,turno,i,j,adyencontrado,jugable):
	adyencontrado,jugable=buscar_ady(tablero,turno,i,j,1,-1,adyencontrado,jugable)
	return adyencontrado,jugable

def buscar_ady_oeste(tablero,turno,i,j,adyencontrado,jugable):
	adyencontrado,jugable=buscar_ady(tablero,turno,i,j,0,-1,adyencontrado,jugable)
	return adyencontrado,jugable

def buscar_ady_noroeste(tablero,turno,i,j,adyencontrado,jugable):
	adyencontrado,jugable=buscar_ady(tablero,turno,i,j,-1,-1,adyencontrado,jugable)
	return adyencontrado,jugable
#_ _ _ fin checks adyacentes

def busca_fichas(tablero,vCoords,tablerocom,turno):
	fichas=0
	encontrado = False
	fichascomidas,encontrado,tablerocom=busca_norte(tablero,vCoords,encontrado,tablerocom,turno)
	fichas+=fichascomidas
	tablero=comer_fichas(tablero,vCoords,tablerocom)
	fichascomidas,encontrado,tablerocom=busca_noreste(tablero,vCoords,encontrado,tablerocom,turno)
	fichas+=fichascomidas
	tablero=comer_fichas(tablero,vCoords,tablerocom)
	fichascomidas,encontrado,tablerocom=busca_este(tablero,vCoords,encontrado,tablerocom,turno)
	fichas+=fichascomidas
	tablero=comer_fichas(tablero,vCoords,tablerocom)
	fichascomidas,encontrado,tablerocom=busca_sureste(tablero,vCoords,encontrado,tablerocom,turno)
	fichas+=fichascomidas
	tablero=comer_fichas(tablero,vCoords,tablerocom)
	fichascomidas,encontrado,tablerocom=busca_sur(tablero,vCoords,encontrado,tablerocom,turno)
	fichas+=fichascomidas
	tablero=comer_fichas(tablero,vCoords,tablerocom)
	fichascomidas,encontrado,tablerocom=busca_suroeste(tablero,vCoords,encontrado,tablerocom,turno)
	fichas+=fichascomidas
	tablero=comer_fichas(tablero,vCoords,tablerocom)
	fichascomidas,encontrado,tablerocom=busca_oeste(tablero,vCoords,encontrado,tablerocom,turno)
	fichas+=fichascomidas
	tablero=comer_fichas(tablero,vCoords,tablerocom)
	fichascomidas,encontrado,tablerocom=busca_noroeste(tablero,vCoords,encontrado,tablerocom,turno)
	fichas+=fichascomidas
	tablero=comer_fichas(tablero,vCoords,tablerocom)
	if fichascomidas==0:
		print('No se pudo encontrar ninguna ficha para voltear')
		repetir=True
	else:
		repetir=False
	return tablero,repetir,tablerocom
	



def buscar_adyacente(tablero,turno,i,j):
	adyencontrado=True
	jugable=True
	adyencontrado,jugable=buscar_ady_norte(tablero,turno,i,j,adyencontrado,jugable)
	adyencontrado,jugable=buscar_ady_noreste(tablero,turno,i,j,adyencontrado,jugable)
	adyencontrado,jugable=buscar_ady_este(tablero,turno,i,j,adyencontrado,jugable)
	adyencontrado,jugable=buscar_ady_sureste(tablero,turno,i,j,adyencontrado,jugable)
	adyencontrado,jugable=buscar_ady_sur(tablero,turno,i,j,adyencontrado,jugable)
	adyencontrado,jugable=buscar_ady_suroeste(tablero,turno,i,j,adyencontrado,jugable)
	adyencontrado,jugable=buscar_ady_oeste(tablero,turno,i,j,adyencontrado,jugable)
	adyencontrado,jugable=buscar_ady_noroeste(tablero,turno,i,j,adyencontrado,jugable)
	if adyencontrado and jugable:
		return adyencontrado
	else:
		return adyencontrado


def verificar_poder_jugar(tablero,turno):
	i=1
	puede_jugar=False
	while i<=8 and not puede_jugar:
		j=1
		while j<=8 and not puede_jugar:
			if buscar_adyacente(tablero,turno,i,j):
				puede_jugar=True
			j+=1
		j+=1
	return puede_jugar

def usuario_juega(tablero,ficha_jugador,tablerocom):
	repetir=True
	while repetir:
		valido=False
		while not valido:
			i=input("Ingrese coordenada vertical")
			j=input("Ingrese coordenada horizontal")
			if verificar_coordenadas_validas:
				valido=True
			else:
				valido=False
		vCoords=[i,j]
		tablero,repetir,tablerocom=busca_fichas(tablero,vCoords,tablerocom,ficha_jugador)
	return tablero, tablerocom

def busca_ficha_pc(tablerocom,i,j,ficha_pc):
	fichas=0
	vCoords=[i,j]
	encontrado = False
	fichascomidas,encontrado,tablerocom=busca_norte(tablero,vCoords,encontrado,tablerocom,ficha_pc)
	fichas+=fichascomidas
	fichascomidas,encontrado,tablerocom=busca_noreste(tablero,vCoords,encontrado,tablerocom,ficha_pc)
	fichas+=fichascomidas
	fichascomidas,encontrado,tablerocom=busca_este(tablero,vCoords,encontrado,tablerocom,ficha_pc)
	fichas+=fichascomidas
	fichascomidas,encontrado,tablerocom=busca_sureste(tablero,vCoords,encontrado,tablerocom,ficha_pc)
	fichas+=fichascomidas
	fichascomidas,encontrado,tablerocom=busca_sur(tablero,vCoords,encontrado,tablerocom,ficha_pc)
	fichas+=fichascomidas
	fichascomidas,encontrado,tablerocom=busca_suroeste(tablero,vCoords,encontrado,tablerocom,ficha_pc)
	fichas+=fichascomidas
	fichascomidas,encontrado,tablerocom=busca_oeste(tablero,vCoords,encontrado,tablerocom,ficha_pc)
	fichas+=fichascomidas	
	fichascomidas,encontrado,tablerocom=busca_noroeste(tablero,vCoords,encontrado,tablerocom,ficha_pc)
	fichas+=fichascomidas

	return fichascomidas



def pc_juega(tablero,tablerocom,ficha_pc):
	fichascomidas=0
	for i in range(1,9):
		for j in range(0,9):
			if tablero[i][j]==ficha_pc:
				if fichascomidas<busca_ficha_pc(tablerocom,i,j,ficha_pc):
					fichascomidas=busca_ficha_pc(tablerocom,i,j,ficha_pc)
					x=i
					y=j
	vCoords=[x,y]
	if fichascomidas>0:
		tablero,repetir,tablerocom=busca_fichas(tablero,vCoords,tablerocom,ficha_pc)
	return tablero,tablerocom
	
def turno_negras(tablero,ficha_jugador,ficha_pc,tablerocom):
	turno='X'
	mostrar_tablero(tablero)
	if verificar_poder_jugar(tablero,turno):
		if ficha_jugador==turno:
			tablero,tablerocom=usuario_juega(tablero,ficha_jugador,tablerocom)
		else:
			tablero,tablerocom=pc_juega(tablero,tablerocom,ficha_pc)
	return tablero,tablerocom

def turno_blancas(tablero,ficha_jugador,ficha_pc,tablerocom):
	turno='O'
	mostrar_tablero(tablero)
	if verificar_poder_jugar(tablero,turno):
		if ficha_jugador==turno:
			tablero,tablerocom=usuario_juega(tablero,vCoords,ficha_jugador,tablerocom)
		else:
			tablero,tablerocom=pc_juega(tablero,tablerocom,ficha_pc)
	return tablero,tablerocom

def juego(tablero,tablerocom,ficha_pc,ficha_jugador):
	juego_continua=True
	while juego_continua:
		tablero,tablerocom=turno_negras(tablero,ficha_jugador,ficha_pc,tablerocom)
		tablero,tablerocom=turno_blancas(tablero,ficha_jugador,ficha_pc,tablerocom)
		juego_continua=verificar_tablero_completo(tablero)

def reescribir_archivo(lista):
	with open("C:\\usuarios.csv",w) as usuarios:
		writer=csv.writer(usuarios)
		usuarios.write(lista)

def cargar_archivo(nombre, puntaje, PJ,PG,PP,PE):
	with open("C:\\usuarios.csv") as usuarios:
		linea = usuarios.readline()
		lista=[]
		while linea.length() > 0:
			linea = linea.split(',')
			if linea[0] == nombre:
				puntaje += int(linea[1])
				PJ += 1
				PG += int(linea[3])
				PP += int(linea[4])
				PE += int(linea[5]) 
			else: 
				lista.append(linea)
			linea = usuarios.readline()
		lineausuario = [nombre,puntaje,PJ,PG,PP,PE]
		lista.append(lineausuario)
	reescribir_archivo(lista)


def resetear_archivo():
	usuarios = open("C:\\usuarios.csv", w)
	usuarios.truncate()
	usuarios.close()
 
 
def reemplazar_archivo():
	path = input('Ingrese el path del nuevo archivo')
	lista = []
	with open(path) as nuevoarchivo:
		linea = nuevoarchivo.readline()
		while linea.length() > 0:
			linea = linea.split(',')
			lista.append(linea)
			linea = nuevoarchivo.readline()
	with open("C:\\usuarios.csv", w) as usuarios:
		writer = csv.writer(usuarios)
		for i in range(0, len(lista)):
			usuarios.writerow(lista[i])
 
 
def ordenar_por_nombre(path):
	with open(path) as archivo:
		linea = archivo.readline()
		lista = []
		while linea.length() > 0:
			lista.append(linea)
			linea = archivo.readline()
		lista.sort(key=lambda nombre: nombre[0])
		return lista
 
 
 
def mostrar_archivo():
	lista = ordenar_por_nombre("C:\\usuarios.csv")
	for i in range(0, len(lista) + 1):
		print('Jugador:{} Puntaje:{} Partidas Jugadas:{} Partidas Ganadas:{} Partidas Perdidas:{} Partidas Empatadas:{}'.format(
			lista[i][0], lista[i][1], lista[i][2], lista[i][3], lista[i][4], lista[i][5]))
 
 
def aparear_archivo():
	path = input('Ingrese el path al nuevo archivo')
	try:
		usuarios = open('C:\\usuarios.csv', w)
		narchivo = open(path)
		fin = ['999']
 
		ordenar_por_nombre(path)
		ordenar_por_nombre("C:\\usuarios.csv")
 
		def leer(archivo):
			arch = archivo.readline()
			if(len(arch) > 0):
				lista = arch.split(',')
				return lista, lista[0]
			else:
				return fin, 999
 
		usuario, nombre = leer(usuarios)
		usuarionuevo, nombrenuevo = leer(narchivo)
 
		while usuario[0] != fin[0] or usuarionuevo != fin[0]:
			if nombre[0] < nombrenuevo[0]:
				usuarios.write(usuario[0] + ',' + usuario[1] + ',' + usuario[2] +
							',' + usuario[3] + ',' + usuario[4] + ',' + usuario[5] + '\n')
				usuario, nombre = leer(usuarios)
			elif nombre[0] > nombrenuevo[0]:
				usuarios.write(usuarionuevo[0] + ',' + usuarionuevo[1] + ',' + usuarionuevo[
							2] + ',' + usuarionuevo[3] + ',' + usuarionuevo[4] + ',' + usuarionuevo[5] + '\n')
				usuarionuevo, nombrenuevo = leer(narchivo)
			elif nombre[0] == nombrenuevo[0]:
				puntaje = int(usuario[1]) + int(usuarionuevo[1])
				partidasjugadas = int(usuario[2]) + int(usuarionuevo[2])
				partidasganadas = int(usuario[3]) + int(usuarionuevo[3])
				partidasperdidas = int(usuario[4]) + int(usuarionuevo[4])
				partidasempatadas = int(usuario[5]) + int(usuarionuevo[5])
				usuarios.write(nombre + ',' + puntaje + ',' + partidasjugadas + ',' +
							partidasganadas + ',' + partidasperdidas + ',' + partidasempatadas + '\n')
				usuario, nombre = leer(usuarios)
				usuarionuevo, nombrenuevo = leer(narchivo)
 
	finally:
		usuarios.close()
        narchivo.close()
 




#-------------------PROGRAMA---------------------------
"""jugador=preguntar_nombre()
ficha_jugador,ficha_pc=asignar_fichas()

tablero=inicializar_matriz()
tablerocom=inicializar_matriz()

juego(tablero,tablerocom,ficha_pc,ficha_jugador)"""


