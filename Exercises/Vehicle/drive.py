''' Tässä moduulissa toteutetaan pelin pääohjelma. '''
from os import name, system, path
from vehicle import Vehicle
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
  mapFolder = path.dirname(path.abspath(__file__))
  map = Map(path.join(mapFolder, values.default_map))


if __name__ == "__main__":
  main()
