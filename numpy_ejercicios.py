import numpy as np   
#imprescindible  #libreria numérica

#Arrays:
a= np.array([1,2,3]) #1D
b= np.array([[1,2],[1,3]]) #2D
c=np.array([[1,2],[2,3],[3,4]]) #3D


#Funciones inicialización:
cero=np.zeros((2,3))  #fila,columna
unos=np.ones((2,3))
full= np.full((2,3),3) #primer paréntesis tamaño del array, fuera del parentesis:Nº que se repite.
rango=np.arange(0,18,2) #primer numero, último no incluido, paso a paso.
##SUPER SIMILAR a RANGE de python.

espacio=np.linspace(0,1,5)  #numero inicio, numero final, pasos TOTALES que va a haber hasta número final.
#----------------------------------------------------

#IMPORTANTEEEEEEE
#Aleatorios:
aleatorio= np.random.rand(3,3)  #da una matriz 3x3 con numeros ALEATORIOS (ENTRE 0-1). (++++++++)
aleatorio2= np.random.randn(3,3)  #da una matriz 3x3 con numeros ALEATORIOS (ENTRE -3 A 3).(--+++-+-)
aleatorio3=np.random.randint(1,10,(2,3))  #primero el rango y dentro de los () tamaño matri<.
#--------------------------------------------------------------------------------------------
#Propiedades:


