"""1. El Conversor de TemperaturasCrea una función llamada celsius_a_fahrenheit que reciba un grado Celsius y devuelva su equivalente en Fahrenheit.Fórmula: $F = C \times 1.8 + 32$"""

def celsius_a_fahrenheit (celsius):
    
    formulaCelsiusAFahrenheit= (celsius * 1.8) +32
    return formulaCelsiusAFahrenheit #ponemos el return en el producto de la función para que cuando explote al finalizar de recorrer no desaparezca.

celsius=int(input())

resultado=celsius_a_fahrenheit(celsius)
print(resultado)




def convertidor(valorUsuario):
    formula= (valorUsuario +98)*32
    return formula
valorUsuario=int(input())
resultado2=convertidor(valorUsuario)
print(resultado2)
#---------------------------------------------------------------

"""4. Calculadora de Promedio
Crea una función llamada promedio que reciba una lista de números y devuelva la media aritmética."""

listanumeros=[] 
def promedio(numeros):
    mediaAritmetica=sum(numeros)/len(listanumeros)
    return mediaAritmetica
   

while True:
    numeros=(input("Introduce un número:")) #Aqui sera formato string
    
    if numeros=="salir":
        break
    numerosInt=int(numeros)    
    listanumeros.append(numerosInt)
print(listanumeros)
resultadoMedia=promedio(listanumeros)