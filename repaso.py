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
        