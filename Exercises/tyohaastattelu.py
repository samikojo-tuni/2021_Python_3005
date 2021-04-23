'''
Seuraavaa tehtävää on käytetty yleisesti työhaastatteluissa ennakkotehtävänä:

Kirjoita funktio, joka ottaa parametrinaan numeron ja palauttaa joko
"Fizz", "Buzz" tai "FizzBuzz" seuraavien ehtojen perusteella: 
- Jos numero on jaollinen kolmella, funktio palauttaa "Fizz"
- Jos numero on jaollinen viidellä, funktio palauttaa "Buzz"
- Jos numero on jaollinen sekä kolmella että viidellä, funktio palauttaa "FizzBuzz"
- Jos numero ei ole jaollinen kolmella eikä viidellä, funktio palauttaa numeron itsensä string-muodossa.

Kiinnitä huomiota ratkaisun selkeyteen ja ylläpidettävyyteen.

Esimerkkiajoja:
fizz_buzz(3) ➞ "Fizz"
fizz_buzz(5) ➞ "Buzz"
fizz_buzz(15) ➞ "FizzBuzz"
fizz_buzz(4) ➞ "4"
'''

def fizz_buzz(number):
  # Virhetarkastelu
  try:
    number = int(number)
  except ValueError:
    print("Parametri ei ollut numero")
    return

  output = ""
  if number % 3 == 0:
    output += "Fizz"
  if number % 5 == 0:
    output += "Buzz"

  if output == "":
    output = str(number)

  return output

def main():
  for i in range(1, 21):
    print(fizz_buzz(i))


if __name__ == "__main__":
  main()
