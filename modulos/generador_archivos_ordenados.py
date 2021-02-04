#Autor: Matias Bangueses
#Numero de legajo: 106566
def reemplazar_acentos(palabra):
    #Esta funcion reemplaza los acentos de una palabra por vocales normales
    indice = 0
    palabra = list(palabra)
    for letra in palabra:
        if letra == 'á':
            palabra[indice] = 'a'
        elif letra == 'é':
            palabra[indice] = 'e'
        elif letra == 'í':
            palabra[indice] = 'i'
        elif letra == 'ó':
            palabra[indice] = 'o'
        elif letra == 'ú':
            palabra[indice] = 'u'
        indice +=1
    return ''.join(palabra)

def limpiar(palabra):
    #limpia unicamente los caracteres antes y despues de la plabra. Ej: "_-?¡palabra.,1;" se convertiría en "palabra"
    primera_letra = 0
    ultima_letra = -1
    palabra = list(palabra)
    if not palabra[primera_letra].isalpha():
        while not palabra[primera_letra].isalpha() and len(palabra) > 1:
            del palabra[primera_letra]
    if not palabra[ultima_letra].isalpha():
        while not palabra[ultima_letra].isalpha() and len(palabra) > 1:
            del palabra[ultima_letra]
    return ''.join(palabra)

def ordenar_palabras(palabras_ordenadas, linea):
    #recibe el archivo cuento en modo lectura y va leyendo linea por linea, retorna una lista de palabras ordenadas alfabeticamente
    #las palabras se van ingresando en la lista de forma ordenada, similar al metodo de insersión
    linea = linea.rstrip('\n').split()
    for palabra in linea:
        palabra = reemplazar_acentos(limpiar(palabra.lower()))
        indice = len(palabras_ordenadas) - 1
        if palabra.isalpha() and palabra > palabras_ordenadas[indice]:
            palabras_ordenadas.append(palabra)
        elif palabra.isalpha():
            repetida = False
            if palabras_ordenadas[indice] == palabra:
                repetida = True
            while indice > 0 and palabras_ordenadas[indice-1] >= palabra:
                indice -= 1
                if palabras_ordenadas[indice] == palabra:
                    repetida = True
            if not repetida:
                palabras_ordenadas.insert(indice, palabra)
    return palabras_ordenadas

def crear_archivo_ordenado(archivo, numero_archivo):
    nombre_nuevo = f'palabras_texto_{numero_archivo}.txt'
    archivo_ordenado = open(nombre_nuevo, 'a')
    linea = archivo.readline()
    #palabras_ordenadas es la lista de palabras que se van a ir ordenando, inicialmente contiene la primer palabra del cuento
    palabras_ordenadas = [linea.strip().split()[0].lower()]
    while linea:
        palabras_ordenadas = ordenar_palabras(palabras_ordenadas, linea)
        linea = archivo.readline()
    for palabra in palabras_ordenadas:
        archivo_ordenado.write(palabra + '\n')
        
def generar_archivos():
    #genera los archivos con las palabras ordenadas alfabeticamente
    nombres = ('Las 1000 Noches y 1 Noche.txt', 'La araña negra - tomo 1.txt', 'Cuentos.txt')
    numero_archivo = 1
    for cuento in nombres:
        archivo = open(cuento, 'r')
        crear_archivo_ordenado(archivo, numero_archivo)
        numero_archivo += 1
        archivo.close()


            