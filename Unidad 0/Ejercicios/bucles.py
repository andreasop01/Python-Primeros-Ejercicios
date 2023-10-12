#bucle while

i=0
while i<10:
    print(f"{i}")
    i+=1
else:
    print(f"Ultima interacion de bucle {i}")

while i<0:
    print(f"{i}")
    i-=1
else:
    print(f"Ultima interacion de bucle {i}")

cadena="Hola que tal esta"

for c in cadena:
    print(c)

for i in range(10):
    print(f"{i}")

for i in range(0,10,2):
    print(f"{i}")

for i in range(10,1,-1):
    print(f"{i}")

for i in range(101):
    if i%2==0:  
        print(f"{i}")