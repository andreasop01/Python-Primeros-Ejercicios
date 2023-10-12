#6. Escriba un programa que pregunte cuantos numeros se van a introducir, pida
#esos numeros, y diga al final cuantos han sido pares y cuantos impares.

cantidades=int(input("Cuantos numeros va a introducir: "))
contPares=0
contImpares=0

for i in range(cantidades):
    numero=int(input("Escriba un numero: "))
    if numero%2==0:
        contPares+=1
    else:
        contImpares+=1

print(f"Hay {contPares} numero pares")
print(f"Hay {contImpares} numero impares")
print("Fin del juego")