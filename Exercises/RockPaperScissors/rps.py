from enums import Choice
from player import HumanPlayer, CPUPlayer

# Ensimmäinen avain on ihmispelaajan valinta.
# Sisempi avain on tietokoneen valinta.
# Lopulliset arvot:
# -   0: Tasapeli
# -   1: Ihminen voittaa
# -  -1: Tietokone voittaa
winningConditions = {
  Choice.ROCK: {
    Choice.ROCK: 0,
    Choice.SCISSORS: 1,
    Choice.PAPER: -1
  },
  Choice.PAPER: {
    Choice.PAPER: 0,
    Choice.ROCK: 1,
    Choice.SCISSORS: -1
  },
  Choice.SCISSORS: {
    Choice.SCISSORS: 0,
    Choice.PAPER: 1,
    Choice.ROCK: -1
  }
}

# Palauttaa seuraavat arvot:
# -   0: Tasapeli
# -   1: Ihminen voittaa
# -  -1: Tietokone voittaa
def resolve(p1result, p2result):
  return winningConditions[p1result][p2result]

def main():
  playerName = input("Give your name: > ")

  # Luodaan pelaajaoliot
  human = HumanPlayer(playerName)
  cpu = CPUPlayer("CPU")

  isQuitting = False
  while not isQuitting:

    humanResult = human.play()
    cpuResult = cpu.play()

    result = resolve(humanResult, cpuResult)

    print(human.name, humanResult)
    print(cpu.name, cpuResult)

    if result == 0:
      print("It's a tie!")
    elif result == 1:
      print(human.name, "wins!")
    else:
      print(cpu.name, "wins!")

    playAgain = input("Play again (y/n)").lower().strip()
    isQuitting = playAgain == "n"


if __name__ == "__main__":
  main()
