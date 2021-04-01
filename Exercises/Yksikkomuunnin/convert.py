# Yksikkömuunnin
#
# Kirjoita sovellus yksikkömuunnosten tekemiseen.
# Ohjelman tulee kysyä käyttäjältä, millaisen yksikkömuunnoksen tämä haluaa tehdä.
# Vaihtoehtoja esimerkiksi:
# t: Lämpötilamuunnos
# v: Valuuttamuunnos
#
# Kun käyttäjä on valinnut haluamansa muunnoksen: kysy käyttäjältä lisätietoja muunnoksesta
# Esim.
# Lämpötilamuunnos:
# 1: Celcius -> Fahrenheit
# 2: Fahrenheit -> Celcius
#
# Tämän valinnan jälkeen kysy käyttäjältä muunnettava arvo
# Esim:
# Anna lämpötila
#
# Lopuksi ohjelma tulostaa muunnoksen tiedot
# Esimerkkiajo (englanniksi, saa toteuttaa myös suomeksi):
# > t
# Convert temperature
# 1: Celcius to Fahrenheit
# 2: Fahrenheit to Celcius
# > 1
# Temperature to convert
# > 20
# 20°C = 68.0°F
# >
#
# Tehtävässä saatte valmiina Conversion-luokan. Peri tästä luokasta muunnoksissa
# tarvittavat luokat. Esimerkki lämpötilalle
# class TemperatureConversion(Conversion)
# Tämä luokka muuntaa lämpötiloja °C ja °F välillä
# convert-funktio muuntaa esim. °C -> °F ja
# convertBack °F -> °C
#
# Tehtävänanto:
# Toteuta ylläkuvattu toiminnallisuus ja tee tuki lämpötilamuunnoksille (°C -> °F ja °F -> °C).
# Lisäominaisuutena voit toteuttaa valuuttamuunnoksia (tuki €, $ ja £)
# Valuuttamuunnokset näiden valuuttojen välillä vaatii siis kolmen luokan toteuttamista,
# muunnokset € ja £ välillä, muunnokset £ ja $ välillä ja muunnokset $ ja € välillä.
#
# Palauta toteuksesi Samille ensi torstaihin klo 12 mennessä osoitteeseen sami.kojo@tuni.fi
# zip-pakattuna tiedostona (koulun sähköposti ei salli .py-tiedostojen lähettämistä).

class Conversion:
  def __init__(self, value):
    self.value = value
    self.source = ""  # Lähdeyksikkö, esim. €
    self.destination = ""  # Kohdeyksikkö, esim. $

  def convert(self):
    ''' Tekee yksikkömuunnoksen lähdeyksiköstä kohdeyksikköön '''
    return 1

  def convertBack(self):
    ''' Tekee yksikkömuunnoksen kohdeyksiköstä lähdeyksikköön '''
    return 1

class TemperatureConversion(Conversion):
  def __init__(self, value):
    super().__init__(value)
    self.source = "°C"
    self.destination = "°F"

  def convert(self):
    return self.value * (9 / 5) + 32

  def convertBack(self):
    return (self.value - 32) * (5 / 9)


def main():
  command = "h"

  while command != "q":
    if command == "h":
      # Tulostetaan ohjeteksti
      print("Yksikkömuunnin", "Komennot:", "t: Lämpötilamuunnos", "c: Valuuttamuunnos",
            "h: Tämä ohjeteksti", "q: Lopettaa sovelluksen", sep="\n")
    elif command == "c":
      print("Valuuttamuunnosta ei ole vielä toteutettu")
    elif command == "t":
      convertTemperature()

    command = input("> ").strip().lower()


def convertTemperature():
  command = 0
  while command != 1 and command != 2:
    print("Tee lämpötilamuunnos", "1: Celcius -> Fahrenheit", "2: Fahrenheit -> Celcius", sep="\n")
    try:
      command = int(input("> "))
    except ValueError:
      command = 0

  value = None
  while value == None:
    print("Syötä muunnettava lämpötila")
    try:
      value = int(input("> "))
    except ValueError:
      value = None

  converter = TemperatureConversion(value)

  if command == 1:
    source = converter.source
    destination = converter.destination
    convertedValue = converter.convert()
  else:
    source = converter.destination
    destination = converter.source
    convertedValue = converter.convertBack()

  print(f"{value}{source} = {convertedValue}{destination}")


if __name__ == "__main__":
  main()
