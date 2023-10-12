#8. Escriba un programa que pregunte cuantos numeros se van a introducir, pida esos
#numeros (que puedan ser decimales) y calcule su suma.

cantidad=int(input("Escriba cuantos numeros va a introducir: "))
suma=0

for i in range(cantidad):
    numero=float(input("Escriba un numero: "))
    suma+=numero
    
print(f"La suma de estos numeros es {numero}")