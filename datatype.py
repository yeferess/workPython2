def analizador (*args, **kwargs):
    enteros=0
    strings=0
    detalles=[]
    resumen = {}
    for x in args: # read single iputs
        if isinstance(x, int):
            enteros+= x
        else:pass # ignore other types

    for key, value in kwargs.items(): # read 
        if isinstance (value, str):
            strings+=1
        detalles.append((key, type(value).__name__))

    #dictionary for export resume    
    resumen['enteros'] = enteros
    resumen['strings'] = strings
    resumen['detalles'] = detalles
    
    return resumen


salida = analizador(1, 3, "hola", edad=30, nombre="jose", apellido = "salas", activo=True)
print(salida)
