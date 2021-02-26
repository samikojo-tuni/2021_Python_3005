'''
Harjoitus 1
Kirjoita rekursiivinen funktio, joka tulostaa Fibonaccin lukujonon n ensimmäistä termiä.
Fibonaccin lukujono muodostuu seuraavasti:
F(n) = 0, kun n = 0
F(n) = 1, kun n = 1
F(n) = F(n-1) + F(n-2), kun n > 1
Lähde: https://fi.wikipedia.org/wiki/Fibonaccin_lukujono

Ratkaisu voi olla helpompi, jos jaat sen useampaan funktioon.
'''
def fibonacci(n):
  if n < 0:
    return None
  elif n <= 1:
    return n

  return fibonacci(n - 1) + fibonacci(n - 2)

def print_fibonacci(n):
  index = 0
  while index < n:
    print(fibonacci(index), end=" ")
    index += 1
  print()


print_fibonacci(20)


'''
Harjoitus 2
Kirjoita funktio, joka laskee numeroiden määrän luvussa rekursiivisesti.
Esim. luvun 10253 tulos on 5 ja luvun 42 tulos on 2.
'''
def number_of_numbers(number):
  if number < 10:
    return 1
  return 1 + number_of_numbers(number / 10)


number = 52389124
print()
print("Numeroita:", number_of_numbers(number))

'''
Harjoitus 3
Alla oleva funktio tarkistaa, onko sana palindromi. Kirjoita funktiosta rekursiivinen versio.
Ratkaisu voi olla helpompi, jos jaat sen useampaan funktioon.

def isPalindrome(word):
   word = word.lower()

   # Poistaa kaikki white spacet
   word = "".join(word.split())

   start = 0
   end = len(word) - 1

   while start <= end:
      if word[start] != word[end]:
         return False
      start += 1
      end -= 1
   return True
'''
def palindrome(word):
  word = word.lower()

  # Poistaa kaikki white spacet
  word = "".join(word.split())

  start = 0
  end = len(word) - 1

  return palindrome_recursive(word, start, end)


def palindrome_recursive(word, start, end):
  if word[start] != word[end]:
    return False

  if start >= end:
    return True

  return palindrome_recursive(word, start + 1, end - 1)


word = "Saippuakivikauppias"
print(f"Onko sana {word} palindromi? {palindrome(word)}")
