from collections import deque
cola= deque()
while True:
    tarea=input("Introduce de una en una las tarea y cuando termine todas las tareas escriba un punto ")
    cola.append(list(tarea))
    
    if tarea == ".":
        break

cola.pop()
print(cola)




