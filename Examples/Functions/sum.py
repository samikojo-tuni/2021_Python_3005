# *-operaattoria käyttäen voidaan määrittää funktio, joka hyväksyy määrittämättömän määrän
# paramerteja [0..*]. Funktiossa parametrit on tallennettu tupleen. Kutsuttaessa parametrit
# erotetaan toisistaan pilkulla
def sum(*numbers):
  result = 0
  for number in numbers:
    result += number
  return result


sum1 = sum(1, 2, 3)
sum2 = sum(1)
sum3 = sum(9, 8, 7, 6, 5, 4, 3, 2, 1)
sum4 = sum()

print(sum1)
print(sum2)
print(sum3)
print(sum4)
