#4. Escriba un programa que pregunte cuantos numeros se van a introducir, pida
#esos numeros, y muestre un mensaje cada vez que un numero no sea mayor que el
#anterior.


cantidad=int(input("Cuantos numeros va a introducir: "))

for i in range(cantidad):
    numero=int(input("Escriba un numero"))

    if i>numero:
        print("Error")
        
print("Fin del  juego")   

    


    
