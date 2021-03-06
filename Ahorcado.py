from modulos import generador_archivos_ordenados as listar_cuentos
from modulos import palabras_ordenadas


def main():#Matias Bangueses
    if not revisar_archivos():
        listar_cuentos.generar_archivos()
    palabras_ordenadas.hacer_lista()
    from modulos import juego
    juego.cantidad_jugadores()
    
    
def revisar_archivos():#Matias Bangueses
    #revisa si las 3 listas hechas a partir de los cuentos están presentes y devuelve un booleano
    cuento = 1
    existe = True
    while cuento < 4 and existe == True:
        archivo = None
        try:
            archivo = open(f'palabras_texto_{cuento}.txt', 'r')
        except FileNotFoundError:
            existe = False
        else:
            if not archivo.readline():
                existe = False
            archivo.close()
        finally:
            cuento += 1
    if existe == False: #si falta 1 o mas archivos, genera 3 txt vacíos
        with open('palabras_texto_1.txt', 'w') as cuento:
            cuento.write('')
        with open('palabras_texto_2.txt', 'w') as cuento:
            cuento.write('')
        with open('palabras_texto_3.txt', 'w') as cuento:
            cuento.write('')
    return existe
    
    
main()