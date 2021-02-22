def leer_registro(fh):
    """
    José Esquivel
    Lee una linea de los registros dados, y si llega al final de este coloca unas ññññ
    para utilizar como error al llegar al final de cada registro
    """
    linea = fh.readline()
    
    if linea:
        registro = linea.rstrip('\n').split(',')
    else:
        registro = ["ññññ"]
    
    return registro


def longitud_palabras(a,largo_palabras):
    """
    José Esquivel
    De cada palabra que llega en la función de hacer_lista()
    y es aceptada para la tabla final se mide su longitud final
    y lo pone en el dicionario con la longitud de la palabras y cuantas tienen esa misma longitud
    """
    
    long_a = len(a[0])
        
    try:
            
        largo_palabras[long_a] += 1
            
    except KeyError:
            
        largo_palabras[long_a] = 1

    return largo_palabras

def palabras_totales(largo_palabras):
    """
    Calcula la cantidad de palabras totales de la lista final.
    José Esquivel
    """
    total = 0  
    for x in largo_palabras:
        total += largo_palabras[x]
    print("La cantidad de palabras totales en la lista final es",total)
    return

def hacer_lista():
    """
    José Esquivel
    Por cada linea leida en el registro, se calcula cual es la menor
    y se coloca en el registro final una por una hasta llegar al final,
    las palabras repetidas no se vuelven a poner
    """
    
    tabla_a_fh = open("palabras_texto_1.txt","r")
    tabla_b_fh = open("palabras_texto_2.txt","r")
    tabla_c_fh = open("palabras_texto_3.txt","r")
    tabla_final_fh = open("palabras.txt","w")
    largo_palabras_fh = open("largo_palabras.txt","w")
    
    a = leer_registro(tabla_a_fh)
    b = leer_registro(tabla_b_fh)
    c = leer_registro(tabla_c_fh)
    
    largo_palabras = {}
    
    while a != ["ññññ"] and b != ["ññññ"] and c != ["ññññ"]:
        
        while a != c and b != c and a != b:
            
            if a < b and a < c:
            
                tabla_final_fh.write('{}\n'.format(a[0]))
                
                largo_palabras = longitud_palabras(a,largo_palabras)
            
                a = leer_registro(tabla_a_fh)
                
            elif b < a and b < c:
            
                tabla_final_fh.write('{}\n'.format(b[0]))
                
                largo_palabras = longitud_palabras(b,largo_palabras)
            
                b = leer_registro(tabla_b_fh)
                    
            elif c < a and c < b:
            
                tabla_final_fh.write('{}\n'.format(c[0]))
                
                largo_palabras = longitud_palabras(c,largo_palabras)
            
                c = leer_registro(tabla_c_fh)
        
        if a == b or b == c:
            
            b = leer_registro(tabla_b_fh)
        
        elif a == c:
            
            c = leer_registro(tabla_c_fh)
    
    largo_palabras_fh.write('{}\n'.format(largo_palabras))
    
    largo_palabras_fh.close()
    tabla_a_fh.close()
    tabla_b_fh.close()
    tabla_c_fh.close()
    tabla_final_fh.close()
    print(largo_palabras)
    palabras_totales(largo_palabras)
    return