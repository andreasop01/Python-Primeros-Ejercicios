#5. Escriba un programa que pregunte cuantos numeros se van a introducir, pida
#esos numeros y escriba cuantos negativos ha introducido.

cantidad=int(input("Cuantos numeros va a introducir: "))
contNeg=0
for i in range(cantidad):
    numero=int(input("Escriba un numero: "))
    
    if numero<0:
        contNeg+=1
        
print(f"Hay {contNeg} numeros negativos")
print("Fin del juego ")
