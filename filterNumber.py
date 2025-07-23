def analizar_numeros(numberList):
    aux_list =[] # create data set of second point
    my_dictionary={}
    
    aux_list = {x for x in numberList if isinstance(x, (float, int))} # compression list
    aux_set = set(aux_list)  # convert list to set
    my_dictionary['max'] = max(aux_set)
    my_dictionary['min'] = min(aux_set)
    my_dictionary['prom'] = round((sum(aux_set) / len(aux_set)),2)
    return my_dictionary
    
entrada = [1, 2, 3, 'a', 'b', 4.5, 6] 
salida = analizar_numeros(entrada)
print(salida)


        