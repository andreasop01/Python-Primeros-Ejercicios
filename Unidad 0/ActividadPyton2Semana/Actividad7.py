#7. Escriba un programa que pida un numero entero mayor que 1 y que escriba si el
#numero es un numero primo o no.

numero=int(input("Escribe un numero entero: "))
cont=0

for i in range(1,numero+1):
    
    if numero%i==0:
        cont+=1
    
if cont==2:
    print(f"El {numero} es primo")
else:
    print(f"El {numero} no esprimo")

    