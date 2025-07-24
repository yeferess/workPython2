def comparar_vocabulary(*frases):
    lista_palabras = []
    palabras_unicas = set()
    palabras_comunes = set()
    contador = 0
    resumen ={}
    
    for frase in frases:
        frase = frase.lower()
        palabras= frase.split()
        lista_palabras.extend(palabras)   

    for palabra in lista_palabras:
        for word in lista_palabras:
            if palabra == word:
                contador += 1
        if contador == 1:
            palabras_unicas.add(palabra)   
        if contador > 1:
            palabras_comunes.add(palabra)
        contador = 0
    resumen['palabras_unicas'] = palabras_unicas
    resumen['palabras_comunes'] = palabras_comunes

    print(resumen)

comparar_vocabulary("Hola mundo", "Python es genial", "Hola Python")
