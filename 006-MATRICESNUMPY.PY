import numpy as np
m=np.array([[1,2],[3,4]])

"""[[1 2]
    [3 4]]"""

#Sumar columnas:  (SUM (AXIS=0))
print(m.sum(axis=0))  #axis=0 → se mueve hacia ABAJO ↓ (por filas)

#Sumar filas: (SUM(AXIS=1))
print(m.sum(axis=1)) #axis=1 → se mueve hacia la DERECHA → (por columnas)

#--------------------------
#Al sumar tenemos que tener cuidado con las dimensiones:
array3=np.array([1,3,4]) #1x3
array4=np.array([[2],[2],[2]]) #3x1

print(array3)
print(array4)