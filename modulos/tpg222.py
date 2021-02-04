import random
from largo_palabras import p
#config.txt
a = []
nombre_jugadores = []
ordenados = []
z = []
s = ""
long= 0
g = 1
h = 0
max_usuarios = 5
max_desaciertos = 7
e = ""
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
    global long
    long = int(input("ingresar la longitud de la palabra: "))
    if long in p:
        if long >= 5: #EDITAR EL WITH OPEN CON SU RESPECTIVA RUTA HACIA tabla_final.txt # EL ENCODING FACILITA EL USO DE LA LETRA Ñ
            with open("c:/Users/marco/OneDrive/Escritorio/UBA/1er cuatrimestre (2do-2020)/Algoritmos y Programacion I/TP/tabla_final.txt", "r", encoding="utf-8") as palab:
                for x in palab:
                    x = x.rstrip("\n")
                    if len(x) == long:
                        a.append(x)
            global s, e
            s = random.choice(a)
            e = len(s) * "_ "
            print(e)
        else:
            logitud_palabra()
    else:
        logitud_palabra()
    return turnos()

letras = ""
d = ""
t = 0
rep = 0
def turnos(): #
    n = 0
    if z == []:
        for u in ordenados:
            z.append({u:[0,0,0,[],0,0,0]})
            #LISTA CON DICCIONARIOS PARA CADA JUGADOR. 
            #{JUGADOR: [ACIERTOS=0, DESACIERTOS=1, PUNTAJE=2, PALABRAS=3, DESACIERTOS PAL=4, ACIERTOS PAL=5, PUNTOS PAL=6]}
    p = 0
    #z[n][u][4] = 0
    for u in ordenados:
        #if z[n][u][1] == 2:
        if z[n][u][4] < 7:              #cambiar el 7 por MAX_DESACIERTOS
            print("turno de", u, "aciertos parciales:", z[n][u][5], "desaciertos parciales:", z[n][u][4], "puntaje parcial:", z[n][u][6])
            def adivinar(letra):
                global e, d, h, t, letras, rep
                rep = 0
                for x in s:
                    if x not in letras:
                        letras += x
                if letra.isalpha():
                    #elif letra in s:
                    if len(letra) == 1 and letra != s:
                        if letra not in d:
                            d += letra
                        else:
                            rep += 1
                        for x in s:
                            if x in d:
                                print(x.upper(), end=" ")
                            else:
                                print("_", end=" ")
                        print(" ")#, len(letras), letras, d, rep)
                    
                    if (len(letra) == 1) and (letra in s) and (rep == 0):
                        print("2 puntos ganados \n")
                        t += 1
                        z[n][u][2] += 2
                        z[n][u][6] += 2
                        z[n][u][0] += 1
                        z[n][u][5] += 1
                    if len(letras) == t:
                        z[n][u][2] += 28
                        z[n][u][6] += 28
                        #z[n][u][0] += 1
                        #z[n][u][5] += 1
                        print(s.upper(), "  ¡¡¡Adivinaste la palabra!!! 30 puntos por adivinar ganados")
                        z[n][u][3].append(letra)
                        h += 1      #continuar con la siguiente funcion. preguntar si se desea seguir jugando, de ser asi, ir a la funcion ORDEN
                    elif letra == s:
                        z[n][u][2] += 30
                        z[n][u][6] += 30
                        z[n][u][0] += 1
                        z[n][u][5] += 1
                        print(s.upper(), "  ¡¡¡Adivinaste la palabra!!! 30 puntos por adivinar ganados")
                        z[n][u][3].append(letra)
                        h += 1      #continuar con la siguiente funcion. preguntar si se desea seguir jugando, de ser asi, ir a la funcion ORDEN
                    elif (len(letra) != 1) or (letra not in s) or (rep != 0):
                        print("1 punto perdido \n")
                        z[n][u][4] += 1
                        z[n][u][1] += 1
                        z[n][u][2] -= 1
                        z[n][u][6] -= 1
                        rep = 0
                    #print(t)
                else:
                    adivinar(input("Ingresar una letra o palabra completa: "))
            adivinar(input("Ingresar una letra o palabra completa: "))
        else:
            print("perdiste el turno salamin.", u, "no juega mas por alcanzar los 2 desaciertos. alejate del teclado \n",)
            p += 1
        #print(z)
        #print("p:", p, " .      n: ", n)
        if h == 1:
            return fin_de_partida()
        n += 1
        if p == len(ordenados):
            print("perdieron todos. gano el grupo UwU. la palabra era: ", s.upper())
            return fin_de_partida()
    turnos()

def fin_de_partida():
    n = 0
    global h, e, d, g, long, s, letras, t, rep
    for u in ordenados:
        print("puntos de:", u, "puntaje total:", z[n][u][2], "aciertos totales:", z[n][u][0], "desaciertos totales:", z[n][u][1])#, "palabras: ", z[n][u][3])
        z[n][u][4] = 0
        z[n][u][5] = 0
        z[n][u][6] = 0
        n += 1
    if g == 1:
        print("ya jugaron", g, "partida.")
    else:
        print("ya jugaron", g, "partidas.")
    g += 1
    e = ""
    d = ""
    letras = ""
    a.clear()
    t = 0
    rep = 0
    h = 0
    long = 0
    s = ""
    f = input("¿Desean seguir jugando? SI: cualquier boton. NO: n       ")
    if f == "n":
        resultados()
    else:
        orden()
    #continuar con la siguiente funcion. preguntar si se desea seguir jugando, de ser asi, ir a la funcion ORDEN

def resultados():
    #ya finalizado el juego se crea el archivo PARTIDA.CSV
    pass

cantidad_jugadores()


#adivinar(input("Ingresar una letra o palabra completa: "))
#logitud_palabra(int(input("ingresar la longitud de la palabra: ")))