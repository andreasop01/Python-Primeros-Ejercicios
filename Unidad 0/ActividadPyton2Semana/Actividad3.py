#3. Escriba un programa que pregunte cuantos numeros se van a introducir, pida
#esos numeros, y muestre un mensaje cada vez que un numero no sea mayor que el
#primero.

cantidad=int(input("Cuantos numeros va a introducir: "))
primero=int(input("Dime el primer numero"))

for i in range(cantidad-1):
    numero=int(input("Escriba un numero"))

    if primero>=numero:
        print("Error")
        
print("Fin del  juego")   

    

