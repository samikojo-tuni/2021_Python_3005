# def-avainsana määrittää funktion
# Funktion parametri(t) eli input. Arvot, jotka funktio ottaa sisään kutsujalta.
# Jos funktio muuttaa ohjelman tilaa, sillä sanotaan olevan sivuvaikutuksia

# Muuttuja alustettu funktion ulkopuolella. Se on ns. globaali muuttuja
isAverageRun = False

def main():
  # Python ei tue funktioiden overloadaamista
  # (saman nimisen funktion määritystä uudestaan eri parametreilla)
  # def sum(num1, num2):
  #   pass

  # def sum(num1, num2, num3):
  #   pass

  numbers = [1, 2, 3, 4, 5]
  # print("Muuttuja ennen:", isAverageRun)
  avg = average(numbers)
  # print("Muuttuja jälkeen", isAverageRun)

  # Funktion sisällä määritetyt muuttujat eivät toimi funktion ulkopuolella
  # print("Summa", result)

  print("Keskiarvo:", avg, sep="\t", end="---")

  numbers2 = [9, 8, 7, 6, 5]
  avg = average(numbers2, False)

  print("Keskiarvo:", avg)


# Python tukee parametrien oletusarvoja. Parametrin oletusarvoa käytetään, jos sille
# ei ole määritetty arvoa funktiota kutsuttaessa.
def average(numbers, printResult: bool = True):
  # global avainsanaa käytetään, jos funktiossa halutaan muuttaa globaalin muuttujan arvoa
  global isAverageRun
  isAverageRun = True

  result = 0
  for number in numbers:
    if result == 0:
      index = 0
    else:
      index += 1

    result += number

  # Vaikka index on määritetty silmukan sisällä,
  # siihen päästään käsiksi myös silmukan ulkosuolella
  # print(index)

  length = len(numbers)
  average = result / length

  if printResult:
    print(average)

  return average  # Funktion paluuarvo eli output. Funktion kutsuja voi käyttää tätä arvoa


avg = average([1, 2, 3, 4])

# Python ei tue main-funktiota, mutta alla olevan määrityksen avulla voimme toteuttaa sitä
# vastaavan toiminnallisuuden
if __name__ == "__main__":
  main()
