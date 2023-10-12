cantidad=int(input("Digame cuantas palabras tiene la lista: "))
lista=[]
cont=0

for i in range(cantidad):
    cont+=1
    palabra=input(f"Digame la palabra {cont}: ")
    lista.append(palabra)

print(f"La lista creada es: {lista}")

palabraf=input("Digame la palabra a buscar: ")


print(f"El elemento {palabraf} aparece {lista.count(palabraf)}")
