'''
Harjoitus 1

Kirjoita funktio, joka ottaa parametrina määrittämättömän määrän numeroita ja 
kertoo ne yhteen. Funktio palauttaa tuloksen paluuarvona.
'''
def multiply(*numbers):
  if len(numbers) == 0:
    # Early exit
    return 0

  result = 1
  for number in numbers:
    result *= number

  return number


'''
Harjoitus 2

Kirjoita funktio, joka palauttaa suurimman luvun, mikä on tallennettu parametrina
saatuun tietorakenteeseen. Mieti myös sopiva arvo palautettavaksi siinä tapauksessa, että 
tietorakenne ei sisällä mitään lukuja.
Toteuta myös vastaava funktio, mikä palauttaa pienimmän luvun tietorakenteessa.
'''
def max(*numbers):
  maxValue = None
  for number in numbers:
    if maxValue == None or number > maxValue:
      maxValue = number
  return maxValue


def min(*numbers):
  minValue = None
  for number in numbers:
    if minValue == None or number < minValue:
      minValue = number
  return minValue


'''
Harjoitus 3

Kirjoita funktio, joka laskee parametrina saadun sanan vokaalisen määrän. Vokaaleja
ovat kirjaimet [a, e, i, o, u, y, ä, ö] (ts. suomen kielen mukaiset vokaalit :).
Funktio palauttaa vokaaleiden määrän.
'''

def vowelCount(word):
  word = word.lower()
  vowels = ("a", "e", "i", "o", "u", "y", "ä", "ö")
  result = 0
  for char in word:
    if char in vowels:
      result += 1

  return result


'''
Harjoitus 4

Kirjoita funktio, joka laskee parametrina välitetyn positiivisen kokonaisluvun
kertoman. Toteuta myös virheiden käsittely.

Määritelmä: "Positiivisen kokonaisluvun n kertoma on luvun n ja kaikkien sitä pienempien 
positiivisten kokonaislukujen tulo, ja se merkitään n!."
(Wikipedia, https://fi.wikipedia.org/wiki/Kertoma)
 
Nollan kertomaksi on sovittu 1.
'''
def factorial(n):
  if n < 0:
    return None
  elif n == 0 or n == 1:
    return 1

  result = 1
  while n > 1:
    result *= n
    n -= 1

  return result


'''
Harjoitus 5

Palindromi
Kirjoita funktio, joka tarkistaa, onko sana palindromi. Palindromi on sana, joka on sama
kirjoitettuna oikein ja väärin päin. Sanan kirjainten koolla ei ole merkitystä.
Oletus: Sana ei sisällä white space -merkkejä (rivinvaihto, välilyönti, tabulaattori).
Bonus: Sana saa sisältää white space -merkkejä, mutta niitä ei oteta huomioon tarkistettaessa,
onko sana palindromi.
'''

def palindromi(word):
  word = word.lower()

  word = "".join(word.split())  # "saip puak\taupp\nias" -> ["saip", "puak", "aupp", "ias"] -> "saippuakauppias"

  start = 0
  end = len(word) - 1

  while start < end:
    startChar = word[start]
    endChar = word[end]

    if startChar != endChar:
      return False

    start += 1
    end -= 1

  return True


print(palindromi("Saip puak\taupp\nias"))
