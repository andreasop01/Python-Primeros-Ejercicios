print("PARES E IMPARES")

numero=int(input("Escriba un numero entero: "))
numero2=int(input(f"Escriba un numero entero mayor o igual que {numero}"))

if numero2>=numero:

    for i in range(numero,numero2+1):
        if i%2==0:
           print(f"El numero {i} es par")
        else:
           print(f"El numero {i} es impar")

else:
    print(f"¡Le he pedido un número entero mayor o igual que {numero}")

       