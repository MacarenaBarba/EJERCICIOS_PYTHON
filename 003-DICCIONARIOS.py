#1:Crear un diccionario.
persona={"nombre":"María", "edad":23, "trabajo":"consultora","nacionalidad":"francesa"}
print(persona)

#a.Acceder a nombre:
print(persona["nombre"])

#b.Modificar valores:
persona["nombre"]="sandra"
print(persona["nombre"])

#c.añadir
persona["nueva_clave"]="nuevo_valor"

#d.Eliminar una clave:
persona.pop("nueva_clave")

#e.Recorrer diccionario
for clave, valor in persona.items():
    print(f"{clave}: {valor}")

#-------------------------------------------------
#2. Contar cuantas veces aparece una palabra.
conteo={}
frase="lechuga pie pie mallorca lechuga nariz"
palabra=frase.split()
for i in palabra:
    if i in conteo:
        conteo[i]+=1
    else:
        conteo[i]=1
print(conteo)        