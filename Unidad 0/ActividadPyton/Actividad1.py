import random

print("Juego de dados")

dado1=int(random.randrange(1,7))
dado2=int(random.randrange(1,7))

jugadores=("Alberto","Barbara")

print(f"{jugadores[0]},ha sacado un {dado1}")
print(f"{jugadores[1]},ha sacado un {dado2}")

if dado1>dado2:
    print(f"{jugadores[0]},ha ganado")

elif dado1<dado2:
    print(f"{jugadores[1]},ha ganado")
else:
    print("Han empatado")