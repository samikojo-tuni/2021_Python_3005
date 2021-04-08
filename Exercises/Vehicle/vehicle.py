from values import Terrain, Direction
from map import Map

class Vehicle:
  ''' Kantaluokka kaikille ajoneuvoille '''

  def __init__(self, speed, x, y):
    ''' Määrittää ajoneuvon ominaisuudet.

        Parametrit:
        speed: ajoneuvon nopeus peliruutuina / vuoro
        x: ajoneuvon x-koodrinaatti kartalla
        y: ajoneuvon y-koordinaatti kartalla
    '''
    self.speed = speed
    self.position = (x, y)

    self.name = ""
    self.symbol = " "

    self.InitAllowedTerrains()

  def InitAllowedTerrains(self):
    ''' Määrittää millaisessa maastossa ajoneuvolla voi ajaa. Arvot values.Terrain-enumin arvoja.
    '''
    self.allowedTerrains = [Terrain.NONE]

  def GetName(self):
    ''' Palauttaa ajoneuvon nimen. '''
    return self.name

  def GetSymbol(self):
    ''' Palauttaa symbolin, jolla ajoneuvo piirretään karttaan. '''
    return self.symbol

  def Move(self, direction: Direction, map: Map):
    ''' Liikuttaa ajoneuvoa parametrin direction suuntaan

        Liikuttaa ajoneuvoa haluttuun suuntaan, mutta vain, jos kyseisessä suunnassa on sallittua maastoa.
        Kohdekoordinaatti riippuu ajoneuvon nopeudesta. Osa ajoneuvoista voi liikkua vain tietynlaisessa 
        maastossa. Varmista, että ajoneuvo ei liiku sellaiseen maastoon, jossa se ei voi kulkea.
        Ajoneuvo liikkuu sen nopeuden määrittämän määrän ruutuja vuoron aikana suuntaan direction, mutta
        kuitenkin siten, että se ei päädy koskaan sellaiselle maastolle, missä se ei voi kulkea.
        Esimerkiksi jos ajoneuvon nopeus on kaksi, mutta kulkusuunnassa on vain yksi ruutu maastoa, jossa
        ajoneuvo voi kulkea, liikkuu ajoneuvo vain yhden ruudun.
    '''
    pass  # Korvaa tämä funktion toteutuksella

class Car(Vehicle):
  def __init__(self, x, y):
    super().__init__(2, x, y)
    self.name = "Auto"
    self.symbol = "A"

  def InitAllowedTerrains(self):
    # Auto kulkee vain maalla
    self.allowedTerrains = [Terrain.GROUND]

class Plane(Vehicle):
  def __init__(self, x, y):
    super().__init__(3, x, y)
    self.name = "Lentokone"
    self.symbol = "L"

  def InitAllowedTerrains(self):
    self.allowedTerrains = [Terrain.GROUND, Terrain.WATER]

class Boat(Vehicle):
  def __init__(self, x, y):
    super().__init__(1, x, y)
    self.name = "Vene"
    self.symbol = "V"

  def InitAllowedTerrains(self):
    self.allowedTerrains = [Terrain.WATER]
