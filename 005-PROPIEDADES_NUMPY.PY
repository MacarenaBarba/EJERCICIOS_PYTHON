#NUESTRO ARRAY PARA EL EJERCICIOS:
import numpy as np
a=np.array([[2,3],[2,4],[2,9]])
print(a)

#A.Forma:
print("la forma de mi array es:")
print(a.shape)   #.shape

#B.Número de Dimensiones:
print("el numero de dimensiones es:")
print(a.ndim)  #.ndim

#C.Número de elementos:
print("el numero de elementos es:")
print(a.size)   #size

#D.Tipo de datos:
print("el tipo de dato es:")
print(a.dtype)   #dtype

#-------------------------------------------------------------------------------------
#E. Indexación se puede realizar:
b=np.array([10,20,30,40])
#b[0]  daría 10
#b[-1]  daría 40
#b[1:3] daría [20,30]


c=np.array([[1,5,3],[1,2,56],[8,4,7]])  #2D
#       col   0  1  2
# fila 0   [[ 1  5  3]
# fila 1    [ 1  2 56]    ESTA SERIA SU MATRIZ
# fila 2    [ 8  4  7]] 

#c[0,0] -----> DARÁ 1
#c[0,1] ----->dará 5
#c[2,0]----------> dará 8
#c[-1,-1]------> dará 7

#Seleccionar filas enteras: 
#c[2] ----------> selecciona la fila dos 

#Seleccionar columnas enteras: 
#c[:,2]---------->selecciona la columna dos


#Slicings:
#c[0:1,2:3]
#-----------------------------------------------------------------------------------

#OPERACIONES NUMERICAS:
array1=np.array([1,2,3])
array2=np.array([4,5,6])

print("la suma de las dos es:")
print(array1+array2)

print("la resta de ambas es:")
print(array1-array2)

print("la multiplicación es:")
print(array1*array2)

print("la raíz cuadrada es:")
print(np.sqrt(array1))

#---------------------------------------------------------------------
#AGREGACIONES:
x=np.array([1,2,3,4,5])

#A.SUMA DEL ARRAY:
print("la suma del conjunto del array es:")
print(x.sum())    #.sum()

#B.LA MEDIA DEL ARRAY:
print("la media del array es:")  #.mean()
print(x.mean())

#C.LA DESVIACIÓN ESTÁNDAR.
print("la desviación estándar es:")   #.std()
print(x.std())