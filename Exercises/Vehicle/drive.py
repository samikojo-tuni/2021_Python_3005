''' Tässä moduulissa toteutetaan pelin pääohjelma. '''
from os import name, system, path
from vehicle import Boat, Car, Plane, Vehicle
import values
from map import Map

def clear():
  '''
  Tyhjentää komentokehotteen. Tukee Windows ja Linux/macOS järjestelmiä.
  '''
  if name == "nt":
    # Windows
    system("cls")
  else:
    # Jokin muu (Linux/macOS)
    system("clear")

def main():
  # TODO: Lue kartan sijainti komentoriviparametrina

  # Karttatiedoston sisältävän kansion polku
  mapFolder = path.dirname(path.abspath(__file__))
  # Karttatiedoston absoluuttinen polku kiintolevyllä
  mapFile = path.join(mapFolder, values.default_map)

  map = Map(mapFile)

  car = Car(1, 1)
  plane = Plane(3, 3)
  boat = Boat(7, 3)

  # Muuttuja, johon valittu ajoneuvo on tallennettu
  currentVehicle = car

  # Käyttäjän syöttämä komento, alustetaan tyhjäksi
  command = ""
  while command != "q":
    clear()  # Tyhjennetään komentokehote jokaisen komennon jälkeen

    map.Draw(car, plane, boat)

    print("Liikutettava ajoneuvo:", currentVehicle.GetName())

    command = input("Syötä komento > ").strip().lower()

    # Sallitut komennot:
    # - up: liikuttaa ajoneuvoa ylöspäin
    # - down: liikuttaa ajoneuvoa alaspäin
    # - left: liikuttaa ajoneuvoa vasemmalle
    # - right: liikuttaa ajoneuvoa oikealle
    # - c: käytä autoa
    # - p: käytä lentokonetta
    # - b: käytä venettä
    # - q: sulje sovellus
    if command == "up":
      currentVehicle.Move(values.Direction.UP, map)
    elif command == "down":
      currentVehicle.Move(values.Direction.DOWN, map)
    elif command == "left":
      currentVehicle.Move(values.Direction.LEFT, map)
    elif command == "right":
      currentVehicle.Move(values.Direction.RIGHT, map)
    elif command == "c":
      currentVehicle = car
    elif command == "b":
      currentVehicle = boat
    elif command == "p":
      currentVehicle = plane


if __name__ == "__main__":
  main()
