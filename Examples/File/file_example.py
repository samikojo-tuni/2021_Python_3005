filePath = "Python-3005/Examples/File/fruits.txt"
fruits = []

# Avataan tiedosto lukutilassa
file = open(filePath, "r")
for row in file:
  # Luetaan tiedosto rivi riviltä
  row = row.strip()
  if row != "":
    fruits.append(row)
file.close()

for fruit in fruits:
  print(fruit)

fruits.append("Mango")
fruits.append("Kiwi")

output = ""
for fruit in fruits:
  output += (fruit + "\n")

# Avataan tiedosto kirjoittamista varten. tila "a" kirjoittaa uuden datan tiedoston loppuun, kun tila "w"
# ylikirjoittaa tiedoston
file = open(filePath, "w")
file.write(output)

file.close()
