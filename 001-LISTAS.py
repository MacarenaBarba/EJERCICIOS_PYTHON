#Vamos a realizar ejercicios relacionados con las listas.

"""EJERCICIO 1: El Supermercado
Crea una lista llamada compra que contenga: "pan", "leche", "huevos" y "manzanas"."""

compra=["pan","leche","huevos","manzanas"]
#A.Imprime el segundo elemento de la lista.
print(compra[1])
#B.Añade "chocolate" al final de la lista.
compra.append("chocolate")
print(compra)
#C.Sustituye "leche" por "avena".
compra[1]="avena"
print(compra)


"""Ejercicio 2: Ranking de Notas
Tienes esta lista de notas: notas = [7, 4, 9, 3, 8, 2, 10]."""

#A.Ordena la lista de menor a mayor.
notas=[7, 4, 9, 3, 8, 2, 10]
notas.sort()
print(notas)

#B.Elimina la nota más baja (el primer elemento tras ordenar).

notas.pop(6)
print(notas)
#C.Imprime cuántos elementos tiene la lista ahora usando len().
len(notas)

"""Ejercicio 3: El Invitado Impuntual
Crea una lista invitados = ["Ana", "Juan", "Pedro"]."""

#A."Luis" llega tarde y quiere ponerse el primero de la lista (usa .insert()).

invitados_list =["Ana","Juan", "Pedro"]
invitados_list.insert(0,"Luis")
print(invitados_list)

#B."Pedro" se cansa de esperar y se va. Elimínalo de la lista usando su nombre.
invitados_list.remove("Pedro")
print (invitados_list)

#C.Imprime la lista final.
print (invitados_list)


"""Ejercicio 4: Bucles y Listas (Nivel Medio-Bajo)
Dada la lista numeros = [1, 2, 3, 4, 5]:

Crea un bucle for que recorra la lista y multiplique cada número por 10.

Imprime el resultado de cada operación."""
numeros=[1,3,3,4,5]
for i in numeros:
    print(f"El resultado de la multiplicación de {i} y 10 es:")
    print(i*10)

    
#------------------------------------------------------------------
"""Ejercicio 5: Buscador de Colores
Crea una lista con 5 colores.

Pide al usuario que escriba un color por teclado (input).

Dile si ese color está en tu lista o no (pista: usa el operador in)."""
colores=["azul","verde","naranja","amarillo","salmón"]
dato= input("El color introducido es:").lower()

if dato in colores: 
    print(f"El color {dato} se encuentra en la lista de colores")
else:
    print(f"El color {dato} NO se encuentra en la lista de colores")
#---------------------------------------------------------------------

"""Ejercicio 6: El Filtro de Seguridad
Tienes una lista de nombres: invitados = ["Ana", "Francisco", "Luis", "Marta", "Ian", "Beatriz"].

Reto: Crea una nueva lista que contenga solo los nombres que tengan 5 letras o más. Imprime la lista resultante."""
#lista invitados:
invitados = ["Ana", "Francisco", "Luis", "Marta", "Ian", "Beatriz"]

#Crear una lista con todos los nombres que tengan 5 letras o más:
invitados_5=len(invitados)
nombre5=[]

for i in invitados:
    if len(i)>=5:
        nombre5.append(i)
    else:
        print(f"{i} no esta en la lista de los nombres largos")

print(nombre5)