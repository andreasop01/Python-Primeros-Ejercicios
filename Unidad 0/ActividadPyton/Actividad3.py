import random

print("Juego del Quince")

cartas1=(random.randrange(1,11), random.randrange(1,11),random.randrange(1,11))
cartas2=(random.randrange(1,11), random.randrange(1,11),random.randrange(1,11))
jugadores=("Gloria","Hector")

print(f"{jugadores[0]},ha sacado un {cartas1[0]},un {cartas1[1]},y un {cartas1[2]}")
print(f"{jugadores[1]},ha sacado un {cartas2[0]},un {cartas2[1]},y un {cartas2[2]}")

if sum(cartas1)<=15:
    print(f"Ha ganado,{jugadores[0]}")

elif sum(cartas2)<=15:
    print(f"Ha ganado,{jugadores[1]}")

elif sum(cartas1)==sum(cartas2) and sum(cartas1)<=15 and sum(cartas2)<=15:
    print("Han empatado")

else:
    print("Ambos pierden")