def analizar_numeros(numberList):
    aux_list ={} # create data set of second point
    my_dictionary={}
    
    # normal for and comparation if
    # for x in numberList:
    #     if (isinstance(x, (float, int))):
    #         aux_list.append(x)

    aux_list = {x for x in numberList if isinstance(x, (float, int))} # compression list
      
    my_dictionary['max'] = max(aux_list)
    my_dictionary['min'] = min(aux_list)
    my_dictionary['prom'] = round((sum(aux_list)) / len(aux_list),2)
    return my_dictionary
    
entrada = [1, 2, 3, 'a', 'b', 4.5, 6] 
salida = analizar_numeros(entrada)
print(salida)


        