# Lista määritetään hakasulkeilla
cars = ["Toyota", "Mazda", "Ford", "Audi"]

print(cars)

# Append lisää alkion listan loppuun
cars.append("Jeep")

print (cars)

# Insert lisää alkion tiettyyn listan indeksiin
cars.insert(2, "Fiat")
print(cars)

# Pop poistaa alkion listasta parametrina saadun indeksin kohdalta. Jos indeksiä ei määritetä,
# poistetaan listan viimeinen alkio
deleted = cars.pop()
print(deleted)

deleted = cars.pop(1)
print (deleted)

# Del voi poistaa listasta alkioita tietystä indeksistä tai indeksiväliltä tai koko listan
del cars[1:3]
print(cars)

# Clear tyhjentää listan, mutta ei poista sitä
cars.clear()

# del cars
print(cars)
