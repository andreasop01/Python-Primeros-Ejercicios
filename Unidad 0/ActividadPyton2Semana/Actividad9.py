#9. Escriba un programa que pida dos numeros enteros y escriba la suma de todos los
#enteros desde el primer numero hasta el segundo.

numero1=int(input("Escribe un numero: "))
numero2=int(input("Escribe otro numero: "))
suma=numero1
print(f"> {numero1}",end="")
for i  in range(numero1+1,numero2+1):
    suma+=i
    print(f"+ {i}",end="")

print(f" {suma}")



