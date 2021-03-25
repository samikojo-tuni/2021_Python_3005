from enums import Choice
import random

# Pelaajan toiminnallisuuden toteuttava kantaluokka.
class Player():
  def __init__(self, name):
    self.name = name

  # Palauttaa arvon None. Ylikirjoitetaan HumanPlayer ja CPUPlayer luokissa
  def play(self):
    return None

class HumanPlayer(Player):
  def play(self):
    # Käyttäjän valinta tallennetaan tähän muuttujaan. NONE kuvaa sitä, että käyttäjä ei ole vielä tehnyt valintaa
    choice = Choice.NONE

    while choice == Choice.NONE:
      try:
        choiceInt = int(input("Give your choice (1=Rock, 2=Paper, 3=Scissors): "))
        choice = Choice(choiceInt)
      except ValueError:
        print("Illegal input, give a number between 1 and 3")
        choice = Choice.NONE
      except KeyboardInterrupt:
        raise KeyboardInterrupt()
      except:
        print("Unknown error! Please write a bug report.")
        choice = Choice.NONE

    return choice

class CPUPlayer(Player):
  def play(self):
    # Käyttämällä random.randint:ä, b (3) on mukana tulosjoukossa
    return Choice(random.randint(1, 3))
