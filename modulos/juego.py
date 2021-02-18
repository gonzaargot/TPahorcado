import random
from operator import itemgetter
from largo_palabras import largo_palabras
from modulos import configuracion
lista_palabras = []      
nombre_jugadores = []
ordenados = []
puntos_jugador = []
palabra_azar = ""
longitud_palabra= 0
partidas = 1
ganador = 0
palabra_oculta = ""
letras_no_rep = ""
letras_adivinadas = ""
n_letras_faltantes = 0
repetido = 0
MAX_USUARIOS, LONG_PALABRA_MIN, MAX_DESACIERTOS, PUNTOS_ACIERTOS, PUNTOS_DESACIERTOS, PUNTOS_ADIVINA = configuracion.configuracion()

def dictalista(listadict):
    """ Funcion que toma una lista de diccionarios [{},{},...] y devuelve una lista de listas de esos diccionarios, siendo la clave del diccionario el primer valor de cada sublista.[[],[],].
    ej.: Para: [{"clave1":[1,2,3]},{"clave2":[3,4,5]}]
    Devuelve: [["clave1",1,2,3],["clave2",3,4,5]]"""
    lista = []
    i = 0
    for jugador in listadict:
        for nombre in jugador:
            lista.append([nombre])
            for datos in jugador[nombre]:
                lista[i].append(datos)
        i += 1
    return lista

def cantidad_jugadores():
    jugadores = input("Cuantos personas van a jugar: ")
    if jugadores.isnumeric():
        if int(jugadores) <= MAX_USUARIOS:
            return solicitar_nombres(jugadores)
        else:
            print('La cantidad maxima de jugadores es ', MAX_USUARIOS)
    else:
        print('Tenes que ingresar un numero')       
    return cantidad_jugadores()

def solicitar_nombres(jugadores):
    cantidad = 0
    while cantidad != int(jugadores):
        nom = input('Nombre del jugador: ')
        nombre_jugadores.append(nom)
        cantidad += 1
    return orden()     
    
def orden():
    for i in range(len(nombre_jugadores)):
        elegido = random.choice(nombre_jugadores)
        nombre_jugadores.remove(elegido)
        ordenados.append(elegido)
    print('El orden de los jugadores es el siguente: ', ordenados)
    return logitud_palabra()

def ordenad():
    segundo_orden = []
    segundo_orden.clear()
    temporal = {}
    global ganador, ordenados
    if ganador == 1:
        jugador = 0
        for nombre in ordenados:
            if puntos_jugador[jugador][nombre][7] == 1:
                segundo_orden.append(nombre)
                puntos_jugador[jugador][nombre][7] = 0
            jugador += 1
        jugador = 0        
        for nombre in ordenados:
            puntos = puntos_jugador[jugador][nombre][2]
            juga = nombre 
            temporal[juga] = puntos
            jugador += 1
        tempo_orden = sorted(temporal.items(), key=itemgetter(1), reverse = True)
        for i in tempo_orden:
            list(i)
            if i[0] not in segundo_orden:
                segundo_orden.append(i[0])
        print('El nuevo orden es: ', segundo_orden)
        ordenado = segundo_orden
        temporal.clear()
    else:
        jugador = 0
        for nombre in ordenados:
            puntos = puntos_jugador[jugador][nombre][2]
            juga = nombre 
            temporal[juga] = puntos
            jugador += 1
        tempo_orden = sorted(temporal.items(), key=itemgetter(1), reverse = True)
        for i in tempo_orden:
            list(i)
            if i[0] not in segundo_orden:
                segundo_orden.append(i[0])
        print('El nuevo orden es: ', segundo_orden)
        ordenado = segundo_orden
        temporal.clear()       
    ganador = 0
    return logitud_palabra()

def logitud_palabra():
    global longitud_palabra
    longitud_palabra = input("Ingresar la longitud de la palabra: ")
    if longitud_palabra.isnumeric():
        if int(longitud_palabra) in largo_palabras:
            if int(longitud_palabra) >= LONG_PALABRA_MIN:
                with open("palabras.txt", "r") as palab:
                    for x in palab:
                        x = x.rstrip("\n")
                        if len(x) == int(longitud_palabra):
                            lista_palabras.append(x)
                global palabra_azar, palabra_oculta
                #print(lista_palabras ,len(lista_palabras))
                palabra_azar = random.choice(lista_palabras)
                palabra_oculta = len(palabra_azar) * "_ "
                print(palabra_oculta)
        else:
            logitud_palabra()
    else:
        print('Tenes que ingresar un numero')
        logitud_palabra()
    return turnos()

def turnos(): #
    jugador = 0
    if puntos_jugador == []:
        for nombre in ordenados:# [ {"eee":[]}   , {"ss":[] }   ,    {"q":[]}      ]
            puntos_jugador.append({nombre:[0,0,0,[],0,0,0,0]})
            #LISTA CON DICCIONARIOS PARA CADA JUGADOR. 
            #{JUGADOR: [ACIERTOS=0, DESACIERTOS=1, PUNTAJE=2, PALABRAS=3, DESACIERTOS PAL=4, ACIERTOS PAL=5, PUNTOS PAL=6, POSICION = 7]}
    perdedor = 0
    #puntos_jugador[jugador][nombre][4] = 0
    for nombre in ordenados:
        #if puntos_jugador[jugador][nombre][1] == 2:
        if puntos_jugador[jugador][nombre][4] < MAX_DESACIERTOS:              #cambiar el 7 por MAX_DESACIERTOS
            print("turno de", nombre, "aciertos parciales:", puntos_jugador[jugador][nombre][5], "desaciertos parciales:", puntos_jugador[jugador][nombre][4], "puntaje parcial:", puntos_jugador[jugador][nombre][6])
            def adivinar(letra):
                global palabra_oculta, letras_adivinadas, ganador, n_letras_faltantes, letras_no_rep, repetido
                repetido = 0
                for x in palabra_azar:
                    if x not in letras_no_rep:
                        letras_no_rep += x
                if letra.isalpha():
                    #elif letra in palabra_azar:
                    if len(letra) == 1 and letra != palabra_azar:
                        if letra not in letras_adivinadas:
                            letras_adivinadas += letra
                        else:
                            repetido += 1
                        for x in palabra_azar:
                            if x in letras_adivinadas:
                                print(x.upper(), end=" ")
                            else:
                                print("_", end=" ")
                        print(" ")#, len(letras_no_rep), letras_no_rep, letras_adivinadas, repetido)
                    
                    if (len(letra) == 1) and (letra in palabra_azar) and (repetido == 0):
                        print("2 puntos ganados \n")
                        n_letras_faltantes += 1
                        puntos_jugador[jugador][nombre][2] += PUNTOS_ACIERTOS
                        puntos_jugador[jugador][nombre][6] += PUNTOS_ACIERTOS
                        puntos_jugador[jugador][nombre][0] += 1
                        puntos_jugador[jugador][nombre][5] += 1
                    if len(letras_no_rep) == n_letras_faltantes:
                        puntos_jugador[jugador][nombre][2] += PUNTOS_ADIVINA
                        puntos_jugador[jugador][nombre][6] += PUNTOS_ADIVINA
                        puntos_jugador[jugador][nombre][7] += 1
                        #puntos_jugador[jugador][nombre][0] += 1
                        #puntos_jugador[jugador][nombre][5] += 1
                        print(palabra_azar.upper(), "  ¡¡¡Adivinaste la palabra!!! 30 puntos por adivinar ganados")
                        puntos_jugador[jugador][nombre][3].append(palabra_azar)
                        ganador += 1      #continuar con la siguiente funcion. preguntar si se desea seguir jugando, de ser asi, ir a la funcion ORDEN
                    elif letra == palabra_azar:
                        puntos_jugador[jugador][nombre][2] += PUNTOS_ADIVINA
                        puntos_jugador[jugador][nombre][6] += PUNTOS_ADIVINA
                        puntos_jugador[jugador][nombre][0] += 1
                        puntos_jugador[jugador][nombre][5] += 1
                        puntos_jugador[jugador][nombre][7] += 1
                        print(palabra_azar.upper(), "  ¡¡¡Adivinaste la palabra!!! 30 puntos por adivinar ganados")
                        puntos_jugador[jugador][nombre][3].append(palabra_azar)
                        ganador += 1      #continuar con la siguiente funcion. preguntar si se desea seguir jugando, de ser asi, ir a la funcion ORDEN
                    elif (len(letra) != 1) or (letra not in palabra_azar) or (repetido != 0):
                        print("1 punto perdido \n")
                        puntos_jugador[jugador][nombre][4] += 1
                        puntos_jugador[jugador][nombre][1] += 1
                        puntos_jugador[jugador][nombre][2] -= PUNTOS_ACIERTOS
                        puntos_jugador[jugador][nombre][6] -= PUNTOS_ACIERTOS
                        repetido = 0
                    #print(n_letras_faltantes)
                else:
                    adivinar(input("Ingresar una letra o palabra completa: "))
            adivinar(input("Ingresar una letra o palabra completa: "))
        else:
            print("perdiste el turno salamin.", nombre, "no juega mas por tener los 7 desaciertos. alejate del teclado \n",)
            perdedor += 1
        #print(puntos_jugador)
        #print("perdedor:", perdedor, " .      jugador: ", jugador)
        #if ganador == 1:
        #    return fin_de_partida()
        jugador += 1
        if perdedor == len(ordenados) or ganador == 1:
            if perdedor == len(ordenados):
                print("perdieron todos. gano el grupo UwU. la palabra era: ", palabra_azar.upper())
            return fin_de_partida()
    turnos()

def fin_de_partida():
    jugador = 0
    global ganador, palabra_oculta, letras_adivinadas, partidas, longitud_palabra, palabra_azar, letras_no_rep, n_letras_faltantes, repetido, lista_palabras
    for nombre in ordenados:
        print("puntos de:", nombre, "puntaje total:", puntos_jugador[jugador][nombre][2], "aciertos totales:", puntos_jugador[jugador][nombre][0], "desaciertos totales:", puntos_jugador[jugador][nombre][1], "palabras: ", puntos_jugador[jugador][nombre][3])
        puntos_jugador[jugador][nombre][4] = 0
        puntos_jugador[jugador][nombre][5] = 0
        puntos_jugador[jugador][nombre][6] = 0
        jugador += 1
    if partidas == 1:
        print("ya jugaron", partidas, "partida.")
    else:
        print("ya jugaron", partidas, "partidas.")
    partidas += 1
    palabra_oculta = ""
    letras_adivinadas = ""
    letras_no_rep = ""
    lista_palabras.clear()
    n_letras_faltantes = 0
    repetido = 0
    longitud_palabra = 0
    palabra_azar = ""
    continuar_juego = input("¿Desean seguir jugando? SI: cualquier boton. NO: n       ")
    if continuar_juego == "n":
        resultados()
    else:
        ordenad()
    
        
    
    



def resultados():
    #ya finaliado el juego se crea el archivo PARTIDA.CSV
    listapuntos = dictalista(puntos_jugador) #Convierte la lista de diccionarios [{"a":[0,0,0..]},{"b":[0,0...]},....] en lista [["a",0,0,...],["b",0,0,....],....]
    listapuntos.sort(key = lambda jugador: jugador[2]) #La ordena por puntaje
    archivo = open("partida.csv","w") #Creacion del archivo partida.csv
    #Comienzo de escritura de partida.csv
    archivo.writelines("Nombre del jugador, Total de aciertos, Total de desaciertos, Puntaje total, Palabras\n")
    for jugador in listapuntos:
        archivo.writelines(jugador[0]+", "+str(jugador[1])+", "+str(jugador[2])+", "+str(jugador[3])+", ")
        for palabras in jugador[4]:
            archivo.writelines(palabras+" ")
        archivo.writelines("\n")
    archivo.close()

cantidad_jugadores()
