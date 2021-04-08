import os
import values

class MapFileNotFoundError(FileNotFoundError):
  pass

class Map:
  '''
  Luokka kuvaa karttaa
  '''

  def __init__(self, mapFilePath):
    self.width = 0
    self.height = 0

    # Luetaan kartan data tiedostosta
    self.ReadMap(mapFilePath)

  def ReadMap(self, filePath):
    self.map = []  # Karttadata tallennetaan 2-ulotteiseen taulukkoon. Taulukko sisältää taulukoita :)

    if not os.path.exists(filePath):
      # jos karttatiedostoa ei löydy, nostetaan tästä poikkeus
      raise MapFileNotFoundError()

    file = open(filePath, "r")

    for row in file:
      # Käydään karttatiedosto läpi rivi riviltä
      row = row.strip()

      if self.width <= 0:
        # Oletetaan kartan jokainen rivi yhtä pitkäksi
        self.width = len(row)

      mapRow = []
      # Luetaan rivi merkki merkiltä ja lisätään oikea maaston tyyppi listaan

      for char in row:
        mapRow.append(self.GetTerrain(char))

      self.map.append(mapRow)

    # Asetetaan kartan korkeus siinä olevien rivien perusteella
    self.height = len(self.map)

    file.close()

  def Draw(self, *vehicles):
    # Piirretaan vaakasuuntainen koordinaatisto
    print("  ", end="")
    for column in range(1, self.width + 1):
      print(column % 10, end="")  # % modulo eli jakojäännösoperaattori
    print()  # Tyhjä print tekee rivinvaihdon

    # Piirretään kartta rivi kerrallaan
    for row in range(self.height):
      print(str((row + 1) % 10), end=" ")  # Piirretään koordinaatti

      for column in range(self.width):
        terrain = self.GetTerrainAt(column, row)  # Kartan kohdassa row, column oleva maastotyyppi
        symbol = self.GetSymbol(terrain)  # Maastotyyppiä vastaava symboli

        # Piirretään oikea symboli, mutta tarkistetaan ensin, onko tutkittavassa koordinaatissa ajoneuvo
        for vehicle in vehicles:
          if vehicle.position[0] - 1 == column and vehicle.position[1] - 1 == row:
            # Koordinaatissa on ajoneuvo
            symbol = vehicle.GetSymbol()
            break  # Hyppää ulos sisimmästä silmukasta

        print(symbol, end="")

      print()  # Rivinvaihto

  def GetTerrain(self, char):
    for key in values.symbols.keys():
      if values.symbols[key] == char:
        return key
    return values.Terrain.NONE

  def GetSymbol(self, terrain: values.Terrain):
    if terrain in values.symbols:
      return values.symbols[terrain]
    raise ValueError

  def GetTerrainAt(self, column, row):
    if column < 0 or row < 0 or column >= self.width or row >= self.height:
      return values.Terrain.NONE  # Tai nostetaan poikkeus
    return self.map[row][column]
