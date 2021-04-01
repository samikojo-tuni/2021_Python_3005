import os
import values

class MapFileNotFoundError(FileNotFoundError):
  pass

class Map:
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

  def GetTerrain(self, char):
    for key in values.symbols.keys():
      if values.symbols[key] == char:
        return key
    return values.Terrain.NONE
