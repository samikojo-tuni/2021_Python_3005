'''
Harjoitus 1
Kirjoita rekursiivinen funktio, joka tulostaa Fibonaccin lukujonon n ensimmäistä termiä.
Fibonaccin lukujono muodostuu seuraavasti:
F(n) = 0, kun n = 0
F(n) = 1, kun n = 1
F(n) = F(n-1) + F(n-2), kun n > 1
Lähde: https://fi.wikipedia.org/wiki/Fibonaccin_lukujono
'''


'''
Harjoitus 2
Kirjoita funktio, joka laskee numeroiden määrän luvussa rekursiivisesti.
Esim. luvun 10253 tulos on 5 ja luvun 42 tulos on 2.
'''


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
