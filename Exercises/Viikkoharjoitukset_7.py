# Harjoitus 1
# Luo luokka Dice, joka määrittää nopan. Luokka ottaa rakentajan parametrina nopan sivujen määrän.
# Kirjoita nopalle funktio roll, joka palauttaa satunnaisen arvon (sivujen lukumäärän mukaan).
#
# Peri luokasta Dice luokat D6, jossa on kuusi sivua ja D20, jossa on 20 sivua.
import random

class Dice:
  def __init__(self, sides):
    self.sides = sides

  def roll(self):
    return random.randint(1, self.sides)

class D6(Dice):
  def __init__(self, ):
    super().__init__(6)

class D20(Dice):
  def __init__(self):
    super().__init__(20)


# Harjoitus 2:
# Kirjoita luokka, joka muuntaa lukuja roomalaisiksi numeroiksi ja päinvastoin
#
# Algoritmi desimaalista roomalaiseksi:
# - Tallenna seuraavat arvot soveltuvaan tietorakenteeseen:
# 1 	I
# 4 	IV
# 5 	V
# 9 	IX
# 10 	X
# 40 	XL
# 50 	L
# 90 	XC
# 100 	C
# 400 	CD
# 500 	D
# 900 	CM
# 1000 	M
#
# - Etsi tietorakenteesta suurin luku, joka on pienempi
#   tai yhtä suuri kuin muunnettava luku. Ota lukua vastaava
#   roomalainen numero talteen ja vähennä muunnettavasta
#   luvusta roomalaista numeroa vastaava arvo
# - Toista tämä, kunnes muunnettava luku on 0
#
# Algoritmi roomalaisesta desimaaliksi:
# - Mieti tätä varten vastaava tietorakenne kuin yllä.
# - Tutki, onko roomalaisen numeron 2 ensimmäistä merkkiä tunnettu
#   roomalainen numero
#   - Jos on, lisää tulokseen merkkiä vastaava desimaalinumero ja
#     siirry roomalaisessa numerossa kaksi merkkiä eteenpäin
#   - Jos ei ole, lisää vain yhtä merkkiä vastaava numero tulokseen
#     ja siirry roomalaisessa numerossa yksi merkki eteenpäin

class RomanConverter:
  def __init__(self):
    self.romans = {1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X", 40: "XL", 50: "L",
                   90: "XC", 100: "C", 400: "CD", 500: "D", 900: "CM", 1000: "M"}
    self.arabic = {}
    for key, value in self.romans.items():
      self.arabic[value] = key

  def ToRoman(self, number):
    result = ""
    previous_value = 0
    previous_character = ""

    while number > 0:
      if number >= 1000:
        number -= 1000
        result += self.romans[1000]
        continue  # Keskeytä silmukan suoritus ja jatka seuraavalle kierrokselle

      for key, value in self.romans.items():
        if number == key:
          number -= key
          result += value
          break

        if key > number:
          number -= previous_value
          result += previous_character
          break

        previous_character = value
        previous_value = key

    return result

  def ToArabic(self, roman):
    index = 0
    result = 0
    length = len(roman)
    while index < length:
      roman_character = roman[index:index + 2]
      if index + 1 < length and roman_character in self.arabic:
        result += self.arabic[roman_character]
        index += 2
      else:
        roman_character = roman[index]
        result += self.arabic[roman_character]
        index += 1
    return result


def main():
  converter = RomanConverter()

  number = 10
  print(f"{number} in roman is {converter.ToRoman(number)}")
  number = 48
  print(f"{number} in roman is {converter.ToRoman(number)}")
  number = 79
  print(f"{number} in roman is {converter.ToRoman(number)}")
  number = 1025
  print(f"{number} in roman is {converter.ToRoman(number)}")
  number = 2021
  print(f"{number} in roman is {converter.ToRoman(number)}")

  roman = "MMXXI"
  print(f"{roman} in arabic is {converter.ToArabic(roman)}")
  roman = "XV"
  print(f"{roman} in arabic is {converter.ToArabic(roman)}")
  roman = "CDXLIII"
  print(f"{roman} in arabic is {converter.ToArabic(roman)}")


if __name__ == "__main__":
  main()
