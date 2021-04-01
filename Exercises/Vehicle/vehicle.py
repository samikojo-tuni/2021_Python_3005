from values import Terrain

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
    self.InitAllowedTerrains()

  def InitAllowedTerrains(self):
    ''' Määrittää millaisessa maastossa ajoneuvolla voi ajaa. Arvot values.Terrain-enumin arvoja.
    '''
    self.allowedTerrains = [Terrain.NONE]

  def GetName(self):
    ''' Palauttaa ajoneuvon nimen. '''
    return ""

  def GetSymbol(self):
    ''' Palauttaa symbolin, jolla ajoneuvo piirretään karttaan. '''
    return " "

  def Move(self, direction, map):
    ''' Toteutetaan Harjoitus 2:na.

        Liikuttaa ajoneuvoa haluttuun suuntaan, mutta vain, jos kyseisessä suunnassa on sallittua maastoa.
        Kohdekoordinaatti riippuu ajoneuvon nopeudesta. Osa ajoneuvoista voi liikkua vain tietynlaisessa 
        maastossa. Varmista, että ajoneuvo ei liiku sellaiseen maastoon, jossa se ei voi kulkea.
        Ajoneuvo liikkuu sen nopeuden määrittämän määrän ruutuja vuoron aikana suuntaan direction, mutta
        kuitenkin siten, että se ei päädy koskaan sellaiselle maastolle, missä se ei voi kulkea.
        Esimerkiksi jos ajoneuvon nopeus on kaksi, mutta kulkusuunnassa on vain yksi ruutu maastoa, jossa
        ajoneuvo voi kulkea, liikkuu ajoneuvo vain yhden ruudun.
    '''
    pass
