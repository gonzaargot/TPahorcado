from modulos import generador_archivos_ordenados as listar_cuentos
from modulos import configuracion


def main():
    if not revisar_archivos():
        listar_cuentos.generar_archivos()
    max_usuarios, long_palabra_min,max_desaciertos, puntos_aciertos, puntos_desaciertos, puntos_adivina = configuracion.configuracion()
    
def revisar_archivos():
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