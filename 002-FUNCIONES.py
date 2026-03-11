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

lista=[]
#liSTA PROMEDIO
while True:
    numero=(input("numero:"))
    if numero.lower()=="salir":
        break
    numeroInt=int(numero) 
    lista.append(numeroInt)   

def promedio(datos):
    media=sum(datos)/len(datos)
    return media

print(promedio(lista))

#-----------------------------
#Define una función recursiva que calcule el factorial de n.
def factorial(valor):
    resultado=1

    for i in range (1,valor + 1):
        resultado=resultado*i
    return resultado

valor=int(input())
print(f"El factorial de {valor} es: {factorial(valor)}")

#--------------------------------------------
## Define una función que cuente las vocales de una cadena:
cadena ="esta es una frase"
listaVocales=[]
vocales=["a","e","i","o","u"]
def contarVocales(cadena):
    #la cadena si la iteramos es por caracter y si usasemos split()estariamos separandola en palabras.
    for i in cadena:
        if i in vocales:
            listavocales=listaVocales.append(i)
            TotalVocales=len(listaVocales)   #no sum porque son letras
    return TotalVocales
print(f"El número totales de vocales es: {contarVocales(cadena)}")

#-----------------------------------------------
# Cuenta cuántas letras mayúsculas y minúsculas hay en una frase
# Devuelve ambos resultados

def size (cadena):
    lower=[]
    higger=[]
    
    
    for i in cadena:
        if  i.islower():
            lower.append(i)
        else:
            higger.append(i)
    return len(lower),len(higger)

cadena=input("el texto a introducir: ")
may,min= size(cadena)
print(f"minúscula:{min}")
print(f"mayúscula{may}")




#-----------------------------------------------------------
# Crea una función llamada calculadora que reciba:
# - dos números
# - una operación (+, -, *, /)
# Y devuelva el resultado

# Esperado:
# calculadora(10, 2, "+")  → 12
# calculadora(10, 2, "-")  → 8
# calculadora(10, 2, "*")  → 20
# calculadora(10, 2, "/")  → 5
# calculadora(10, 0, "/")  → "Error: no se puede dividir entre cero"


def calculadora(numeroA,numeroB,operation):
    
    if operation=="+":
        resultado=numeroA + numeroB
    elif operation=="-":
        resultado=numeroA - numeroB
    elif operation=="*":
        resultado=numeroA * numeroB
    elif operation=="/":
        resultado=numeroA / numeroB        
    else:
        return "Error: operación no válida"
    return resultado

numeroA=int(input("el primer número es:"))
numeroB=int(input("El segundo número es:"))
operation=input("operación (+, -, *, /)")

print(f"el resultado de la calculadora es{calculadora(numeroA,numeroB,operation)}")

#---------------------------------------------------------------------------------------------------
# # Crea una función que reciba una contraseña y compruebe si es segura.
# Una contraseña es segura si tiene:
# - Al menos 8 caracteres
# - Al menos una mayúscula
# - Al menos un número

def validador(password):
    mayuscula=0
    numero=0
    lista=[]
    for i in password:
        if i.isdigit():
            numero+=1
        if i.isupper() :
            mayuscula+=1
    
    if len(password)>=8 and numero>=1 and mayuscula>=1:
        return"la lista es válida"
    else:
        return "La contraseña no es válida"
password=input("Introduce una password: ")
print(validador(password))
        