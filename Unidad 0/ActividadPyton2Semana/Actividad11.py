# 11. Escriba un programa que pregunte cuantos numeros se van a introducir, pida esos
# numeros, y escriba el mayor, el menor y la media aritmetica. Recuerda que la media
# aritmetica de un conjunto de valores es la suma de esos valores dividida por la cantidad de
# valores.

cantidad=int(input("Escriba cuantos numeros va a introducir: "))
numero=int(input("Escriba un numero: "))
suma=numero
min=numero
max=numero

for i in range(cantidad-1):
    numero=int(input("Escriba un numero: "))
    
    suma+=numero
    if numero>max:
        max=numero
    
    if numero<min:
        min=numero

print(f"La media es:{suma/cantidad}")
print(f"El minimo es: {min}")
print(f"El maximo es: {max}")
