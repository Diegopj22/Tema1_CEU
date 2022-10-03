def agregar_una_vez(lista,el):
    
       lista=[]
       for i in lista:
          if el not in lista:
           lista.append(el)
          elif el in  lista:
            break            
            print("Imposible añadir elementos duplicados")
            print(lista)
    
       return lista


print(agregar_una_vez[2342,2])

    
