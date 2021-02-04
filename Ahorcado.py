from modulos import generador_archivos_ordenados as listar_cuentos
from modulos import configuracion

def main():
    listar_cuentos.generar_archivos()
    max_usuarios, long_palabra_min,max_desaciertos, puntos_aciertos, puntos_desaciertos, puntos_adivina = configuracion.configuracion()
    
main()