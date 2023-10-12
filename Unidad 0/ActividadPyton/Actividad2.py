import random

print("Juego de dados(2)")

dado1=(random.randrange(1,7),random.randrange(1,7))
dado2=(random.randrange(1,7),random.randrange(1,7))

jugadores=("Carmen","David")

print(f"{jugadores[0]},ha sacado un,{dado1[0]},y un,{dado1[1]}")
print(f"{jugadores[1]},ha sacado un,{dado2[0]},y un,{dado2[1]}")

if sum(dado1)> sum(dado2):
  print(f"{jugadores[0]},ha ganado")  

elif sum(dado1)<sum(dado2):
  print(f"{jugadores[1]},ha ganado") 

else:
  print("Han empatado")