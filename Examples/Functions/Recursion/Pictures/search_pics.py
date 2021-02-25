# Hakee kuvat rekursiivisesti siitä kansiosta, jossa tämä skripti on ja kaikista sen kansion
# alikansioista.

# Moduulin käyttöönotto. os on Python sisäänrakennettu moduuli, jolla voidaan suorittaa
# erilaisia järjestelmään liittyviä toiminnallisuuksia.
import os

# dir: sen hakemiston tiedostopolku, josta kuvia haetaan
# pics: lista, johon löydettyjen kuvien tiedostopolut tallennetaan
def find_pics(dir, pics):
  # listdir palauttaa parametrina saadun kansion sisältämät tiedostot ja kansiot
  files = os.listdir(dir)
  for file in files:
    # Tiedoston absoluuttinen sijainti kovalevyllä
    path = os.path.join(dir, file)
    if os.path.isdir(path):
      # Tiedosto onkin kansio, etsitään kuvia sen sisältä
      find_pics(path, pics)  # rekursiivinen funktiokutsu
    else:
      # Onko tutkittava tiedosto kuva?
      fileName = file.lower()
      if fileName.endswith(".png") or fileName.endswith(".jpg"):
        # Tiedosto on kuva
        pics.append(path)


# Lista, johon kuvat lisätään
pics = []
# Tämän skriptin sisältävän kansion tiedostopolku
current_dir = os.path.dirname(os.path.realpath(__file__))
# Haetaan kuvat
find_pics(current_dir, pics)

for pic in pics:
  print(pic)
