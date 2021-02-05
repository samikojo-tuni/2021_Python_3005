counter = 10

while counter >= 0:
  print(counter)
  # Muista päivittää ehdossa käytetyn muuttujan arvoa, jotta ohjelma ei jää
  # ikuiseen silmukkaan. Sovelluksesta pääsee pois näppäinyhdistelmällä Ctrl+C
  counter -= 1
  # counter = counter - 1
else:
  # Else suoritetaan, kun silmukan suoritus päättyy ilman, että sitä on
  # eksplisiittisesti keskeytetty
  print("Silmukka päättyy")

# break ja continue
# break keskeyttää silmukan suorittamisen

counter = 10
index = 0  # Pitää kirjaa siitä, montako kertaa silmukka on suoritettu
while counter >= 0:
  if index >= 5:
    break

  index += 1
  print(counter)
  counter -= 1
else:
  # Koska break keskeytti silmukan, else:ä ei suoriteta
  print("Silmukka päättyi")

# Continue keskeyttää tämänhetkisen kierroksen suorittamisen ja siirtyy silmukan seuraavalle
# kierrokselle
start = 0
end = 10

print("\n\n")
while start <= end:
  start += 1
  if start % 2 != 0:  # % modulo eli jakojäännös
    continue
  print(start)

cars = ["Toyota", "Mazda", "Ford", "Audi"]

print("\n")

for car in cars:
  print(car)

print("\n")

sequence = range(len(cars))
for index in sequence:
  print(cars[index])

print("\n")

units = {"tank", "plane", "ship", "dog"}

for unit in units:
  print(unit)
