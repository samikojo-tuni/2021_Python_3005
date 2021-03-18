# Pelaajan toiminnallisuuden toteuttava kantaluokka.
class Player():
  def __init__(self, name):
    self.name = name

  # Palauttaa arvon None. Ylikirjoitetaan HumanPlayer ja CPUPlayer luokissa
  def play(self):
    return None
