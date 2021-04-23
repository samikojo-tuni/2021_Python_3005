# Kirjoita ajastin.
# Ajastin toimii siten, että käyttäjä syöttää ohjelmaan tunnit, minuutit ja sekunnit
# Tämän jälkeen ajastin lähtee laskemaan syötytystä ajasta alaspäin tulostaen uuden
# ajan sekunnin välein komentokehotteeseen.
# Ohjelman suoritus päättyy, kun ajastin käy loppuun.

# Käytä viime viikolla tekemäämme Time-luokkaa ajastimen toteuttamiseen.
# Tutustu myös Pythonin time-moduulin sleep-funktioon.

import time as t  # Aliaksen kautta time-moduulia voidaan käyttää nimellä t
import sys

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

  def Decrease(self):
    self.time -= 1

  def Increase(self):
    self.time += 1

  def ToString(self):
    return f"{self.Hours():02d}:{self.Minutes():02d}:{self.Seconds():02d}"


def main():
  arg_count = len(sys.argv)
  if arg_count == 1:
    # Ei komentoriviparametreja, listan ainut alkio on skriptin nimi
    time = get_time()
  elif arg_count <= 3:
    time = read_time(sys.argv[1])

    message = None
    if arg_count == 3:
      message = sys.argv[2]
  else:
    print("Virheelliset komentoriviparametrit")
    quit()

  countdown(time)

  if message != None:
    print(message)

def read_time(time_string):
  time = time_string.split(":")
  if len(time) == 3:
    try:
      hours = int(time[0])
      minutes = int(time[1])
      seconds = int(time[2])

      return Time(hours, minutes, seconds)
    except ValueError:
      print("Parametrina syötetty aika on virheellinen")
      quit()
  else:
    print("Parametrina syötetty aika on virheellinen")
    quit()


def countdown(time):
  while time.TotalSeconds() > 0:
    print(time.ToString())
    t.sleep(1)
    time.Decrease()


def get_time():
  while True:
    try:
      hours = int(input("Tunnit > "))
      minutes = int(input("Minuutit > "))
      seconds = int(input("Sekunnit > "))

      if minutes < 0 or seconds < 0 or minutes > 59 or seconds > 59:
        print("Syötä laillinen aika!")
        continue

      return Time(hours, minutes, seconds)

    except ValueError:
      print("Syötä laillinen aika!")


if __name__ == "__main__":
  main()
