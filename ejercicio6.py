

def separar(lista):
   '''Función que recibe una lista de enteros y devuelve por un lado, una lista con los números pares y por el otro una lista con los números impares
   ''' 
   numeros_pares=[]
   numeros_impares=[]

   for i in lista:
       if i%2 == 0:
        numeros_pares.append(i)
       else:
        numeros_impares.append(i)
    
   numeros_pares.sort()
   numeros_impares.sort()
   return numeros_pares,numeros_impares

lista=[2,4,7,5,8]
numeros_pares,numeros_impares=separar(lista)
print(numeros_pares)
print(numeros_impares)

    
    




