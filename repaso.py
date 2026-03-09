listaVocales=[]
vocales=["a","e","i","o","u"]
def contarVocales(cadena):
    
    for i in cadena:
        if i in vocales:
            listaVocales.append(i)
            suma=len(listaVocales)
    return suma
cadena: str=input("El texto a introducir:")
print(f"El numero de vocales es: {contarVocales(cadena)}")