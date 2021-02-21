from os import path #Se utiliza para chequear que exista el archivo configuracion.txt
def configuracion():
    """Gonzalo Argot. Funcion que carga los datos de configuracion del juego desde el archivo configuracion.txt. Si hay error en la lectura del archivo, devuelve valores por defecto. """
    max_usuarios = 10 #Valores por defecto
    long_palabra_min = 5
    max_desaciertos = 7
    puntos_aciertos = 2
    puntos_desaciertos = 1
    puntos_adivina = 30    
    if path.exists("configuracion.txt"): #Si existe el archivo configuracion.txt, lo carga y lee los datos.
        archivo = open("configuracion.txt","r")

        lista = ["MAX_USUARIOS","LONG_PALABRA_MIN","MAX_DESACIERTOS","PUNTOS_ACIERTOS","PUNTOS_DESACIERTOS","PUNTOS_ADIVINA"]
        linea = archivo.readline()
        while linea != "": #Iteracion para leer las lineas de configuracion.txt hasta el final.
            for i in range(len(lista)):#Iteracion para saber que parametro de la configuracion se esta leyendo.
                if lista[i] in linea and any(chr.isdigit() for chr in linea): #la condicion "any(chr.isdigit() for chr in linea)" arroja True si alguno de los caracteres de la cadena guardada en la variable linea es un numero. Esto es por si en el archivo configuracion.txt se lee alguna linea que no tenga asignado ningun valor numerico. El valor de esa configuracion queda por defecto.
                    if i == 0: max_usuarios = int(linea.strip(lista[0]))
                    elif i == 1: long_palabra_min = int(linea.strip(lista[1]))
                    elif i == 2: max_desaciertos = int(linea.strip(lista[2]))
                    elif i == 3: puntos_aciertos = int(linea.strip(lista[3]))
                    elif i == 4: puntos_desaciertos = int(linea.strip(lista[4]))
                    elif i == 5: puntos_adivina = int(linea.strip(lista[5]))
            linea = archivo.readline()
        archivo.close()
    else:
        print("\nNo se ha encontrado el archivo configuracion.txt. Utilizando valores de configuracion por defecto...\n\n")#Mensaje de error si no se pueden cargar el archivo configuracion.txt. Se usan los valores por defecto.
 
    return max_usuarios, long_palabra_min,max_desaciertos, puntos_aciertos, puntos_desaciertos, puntos_adivina
