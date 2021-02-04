import random
from largo_palabras import largo_palabras
#config.txt
lista_palabras = []      #
nombre_jugadores = []
ordenados = []
puntos_jugador = []
palabra_azar = ""
longitud_palabra= 0
partidas = 1
ganador = 0
max_usuarios = 5
max_desaciertos = 7
palabra_oculta = ""
letras_no_rep = ""
letras_adivinadas = ""
n_letras_faltantes = 0
repetido = 0

def cantidad_jugadores():
    jugadores = int(input("Cuantos personas van a jugar: "))
    if jugadores <= max_usuarios:
        return solicitar_nombres(jugadores)
    else:
        print('La cantidad maxima de jugadores es ', max_usuarios)
    return cantidad_jugadores()

def solicitar_nombres(jugadores):
    cantidad = 0
    while cantidad != jugadores:
        nom = input('Nombre del jugador: ')
        if len(nom) >= 3:
            nombre_jugadores.append(nom)
            cantidad += 1
        else:
            print("El nombre tiene que tener como minimo 3 caracteres")
    return orden()   
    
def orden():
        for i in range(len(nombre_jugadores)):
            elegido = random.choice(nombre_jugadores)
            nombre_jugadores.remove(elegido)
            ordenados.append(elegido)
        print('El orden de los jugadores es el siguente: ', ordenados)
        return logitud_palabra()



def logitud_palabra():
    global longitud_palabra
    longitud_palabra = int(input("ingresar la longitud de la palabra: "))
    if longitud_palabra in largo_palabras:
        if longitud_palabra >= 5: #EDITAR EL WITH OPEN CON SU RESPECTIVA RUTA HACIA tabla_final.txt # EL ENCODING FACILITA EL USO DE LA LETRA Ñ
            with open("c:/Users/marco/OneDrive/Escritorio/UBA/1er cuatrimestre (2do-2020)/Algoritmos y Programacion I/TP/tabla_final.txt", "r", encoding="utf-8") as palab:
                for x in palab:
                    x = x.rstrip("\n")
                    if len(x) == longitud_palabra:
                        lista_palabras.append(x)
            global palabra_azar, palabra_oculta
            palabra_azar = random.choice(lista_palabras)
            palabra_oculta = len(palabra_azar) * "_ "
            print(palabra_oculta)
        else:
            logitud_palabra()
    else:
        logitud_palabra()
    return turnos()

def turnos(): #
    jugador = 0
    if puntos_jugador == []:
        for nombre in ordenados:# [ {"eee":[]}   , {"ss":[] }   ,    {"q":[]}      ]
            puntos_jugador.append({nombre:[0,0,0,[],0,0,0]})
            #LISTA CON DICCIONARIOS PARA CADA JUGADOR. 
            #{JUGADOR: [ACIERTOS=0, DESACIERTOS=1, PUNTAJE=2, PALABRAS=3, DESACIERTOS PAL=4, ACIERTOS PAL=5, PUNTOS PAL=6]}
    perdedor = 0
    #puntos_jugador[jugador][nombre][4] = 0
    for nombre in ordenados:
        #if puntos_jugador[jugador][nombre][1] == 2:
        if puntos_jugador[jugador][nombre][4] < 7:              #cambiar el 7 por MAX_DESACIERTOS
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
                        puntos_jugador[jugador][nombre][2] += 2
                        puntos_jugador[jugador][nombre][6] += 2
                        puntos_jugador[jugador][nombre][0] += 1
                        puntos_jugador[jugador][nombre][5] += 1
                    if len(letras_no_rep) == n_letras_faltantes:
                        puntos_jugador[jugador][nombre][2] += 28
                        puntos_jugador[jugador][nombre][6] += 28
                        #puntos_jugador[jugador][nombre][0] += 1
                        #puntos_jugador[jugador][nombre][5] += 1
                        print(palabra_azar.upper(), "  ¡¡¡Adivinaste la palabra!!! 30 puntos por adivinar ganados")
                        puntos_jugador[jugador][nombre][3].append(palabra_azar)
                        ganador += 1      #continuar con la siguiente funcion. preguntar si se desea seguir jugando, de ser asi, ir a la funcion ORDEN
                    elif letra == palabra_azar:
                        puntos_jugador[jugador][nombre][2] += 30
                        puntos_jugador[jugador][nombre][6] += 30
                        puntos_jugador[jugador][nombre][0] += 1
                        puntos_jugador[jugador][nombre][5] += 1
                        print(palabra_azar.upper(), "  ¡¡¡Adivinaste la palabra!!! 30 puntos por adivinar ganados")
                        puntos_jugador[jugador][nombre][3].append(palabra_azar)
                        ganador += 1      #continuar con la siguiente funcion. preguntar si se desea seguir jugando, de ser asi, ir a la funcion ORDEN
                    elif (len(letra) != 1) or (letra not in palabra_azar) or (repetido != 0):
                        print("1 punto perdido \n")
                        puntos_jugador[jugador][nombre][4] += 1
                        puntos_jugador[jugador][nombre][1] += 1
                        puntos_jugador[jugador][nombre][2] -= 1
                        puntos_jugador[jugador][nombre][6] -= 1
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
    ganador = 0
    longitud_palabra = 0
    palabra_azar = ""
    continuar_juego = input("¿Desean seguir jugando? SI: cualquier boton. NO: n       ")
    if continuar_juego == "n":
        resultados()
    else:
        orden()
    #continuar con la siguiente funcion. preguntar si se desea seguir jugando, de ser asi, ir a la funcion ORDEN

def resultados():
    #ya finalipuntos_jugadorado el juego se crea el archivo PARTIDA.CSV
    pass

cantidad_jugadores()


#adivinar(input("Ingresar una letra o palabra completa: "))
#logitud_palabra(int(input("ingresar la longitud de la palabra: ")))