numero=int(input("Escriba un numero entero mayor a 0: "))
contador=0

if numero>0:

    for i in range(1,numero+1):
        
        if (numero%i)==0:
            print(f"{i} es divisor")
            contador+=1
    print(f"El numero {numero} tiene {i} divisores")
else:
    print("Error")

