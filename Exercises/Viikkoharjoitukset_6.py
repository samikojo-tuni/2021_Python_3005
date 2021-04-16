'''
Tehtävä 1:

Kirjoita funktio, joka ottaa parametrinaan vuosiluvun ja palauttaa True tai False sen perusteella,
onko vuosi karkausvuosi. Karkausvuosia ovat neljällä jaolliset vuodet. Poikkeuksena tähän on sadalla
jaolliset vuodet. Niiden pitää olla jaollisia myös 400 ollakseen karkausvuosia.
'''
def isLeapYear(year):
  if year % 100 == 0:
    return year % 400 == 0
  return year % 4 == 0


'''
Tehtävä 2:

Kirjoita luokka Time, joka ottaa rakentajan parametrina ajan tunteina, minuutteina ja sekunteina.
Älä käytä apuna aika- tai matematiikkakirjastoja!

Luokassa on seuraavat jäsenfunktiot:
- Hours()
  - palauttaa ajan tuntiosan
- Minutes()
  - palauttaa ajan minuuttiosan
- Seconds()
  - palauttaa ajan sekuntiosan
- TotalHours()
  - palauttaa kokonaisajan tunteina kokonaislukuna
- TotalMinutes()
  - palauttaa kokonaisajan minuutteina kokonaislukuna
- TotalSeconds()
  - palauttaa kokonaisajan sekunteina kokonaislukuna
- ToString()
  - palauttaa ajan muodossa hh:mm:ss

Esimerkki:
aika = Time(12,35,0)
aika.ToString()     # Palauttaa 12:35:00 (Huomaa etunollat)
aika.Hours()        # Palauttaa 12
aika.Minutes()      # Palauttaa 35
aika.Seconds()      # Palauttaa 0
aika.TotalHours()   # Palauttaa 12
aika.TotalMinutes() # Palauttaa 755
aika.TotalSeconds() # Palauttaa 45 300
'''

class Time():
  def __init__(self, hours, minutes, seconds):
    self.time = hours * 3600 + minutes * 60 + seconds  # Kokonaisaika sekunteina

  def TotalSeconds(self):
    return self.time

  def TotalMinutes(self):
    return self.time // 60

  def TotalHours(self):
    return self.time // 3600

  def Hours(self):
    return self.TotalHours()

  def Minutes(self):
    # Tunnissa on 3600 sekuntia. Jakojäännöksessä on tuntiosan jälkeen jäävät sekunnit. Muutetaan ne
    # minuuteiksi jakamalla tulos 60:llä.
    return (self.time % 3600) // 60

  def Seconds(self):
    return self.time % 60

  def ToString(self):
    return f"{self.Hours():02d}:{self.Minutes():02d}:{self.Seconds():02d}"

def main():
  aika = Time(12, 35, 0)
  print(aika.ToString())
  print(aika.TotalHours())
  print(aika.TotalMinutes())
  print(aika.TotalSeconds())
  print(aika.Hours())
  print(aika.Minutes())
  print(aika.Seconds())


if __name__ == "__main__":
  main()
