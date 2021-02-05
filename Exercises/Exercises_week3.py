# Harjoitus 1:
# Suunnittele ja toteuta listan väärinpäin kääntävä algoritmi. Algoritmi toimii siis siten,
# että käännetyn listan ensimmäinen alkio on alkuperäisen listan viimeinen alkio jne.
# Älä käytä list.reverse() funktiota
original = ["Toyota", "Mazda", "Ford", "Audi"]
reversed = []
for index in range(len(original)):
  reversed.append(original[-1 * (index + 1)])

print(reversed)

# Harjoitus 2:
# Suunnittele ja kirjoita algoritmi, joka luo uuden sanan alkuperäisen sanan perusteella siten,
# että alkuperäisestä sanasta otetaan uuteen sanaan joka toinen kirjain.

# Ratkaisu 1
word = "saippuakauppias"
print(word[::2])
# Slicing ja stepping
word = "saippuakauppias"
newWord = word[3:10]

# Ratkaisu 2
word = "saippuakauppias"
index = 0
result = ""
while index < len(word):
  if index % 2 == 0:
    result += word[index]
  index += 1

print(result)

# Harjoitus 3:
# Laske montako parillista ja paritonta numeroa listassa (tai tuplessa) on.
numbers = (3, 1, 6, 3, 4, 7, 0, 6, 3, 2, 6, 8, 3)

odd = 0
even = 0
for num in numbers:
  if num % 2 == 0:
    even += 1
  else:
    odd += 1
print("Even:", even, "Odd:", odd)

# Harjoitus 4:
# Pyydä käyttäjää syöttämään sanoja, kunnes käyttäjä syöttää sanan "stop".
# Lopuksi tulosta kaikki käyttäjän syöttämät sanat (paitsi "stop").
word = ""
word_list = []
stop_word = "stop"

print("Syötä sanoja. Anna sana \"stop\" kun haluat lopettaa")
while word.lower() != stop_word:
  word = input()
  if word.lower() != stop_word:
    word_list.append(word)

print(word_list)

# Harjoitus 5:
# Pyydä käyttäjää syöttämään, monenko luvun keskiarvon tämä haluaa laskea.
# Tämän jälkeen pyydä käyttäjää syöttämään näin monta lukua.
# Laske lopuksi lukujen keskiarvo ja tulosta tämä käyttäjälle
# num = int(input("Syötä numero "))
sum = 0.0

print("Lasketaan keskiarvo. Monenko luvun keskiarvon haluat laskea?")
count = int(input())

for x in range(count):
  number = float(input("Syötä numero "))
  sum += number

average = sum / count  # Huom! Nollalla jako rikkoo tämän!
print(average)

# Harjoitus 6
# Pyydä käyttäjää syöttämään sana. Laske montako kertaa eri kirjaimet esiintyvät sanassa.
# Lopuksi tulosta kirjaimet ja niiden esiintymiskerrat.
# Esimerkkitulosteet:
# Syötä sana > tietokone
# { "t": 2, "i": 1, "e": 2, "o": 1, "k": 1, "n": 1 }
# Vihje: operaattorit in ja not in
# Mietittäväksi: mikä tietorakenne sopii ratkaisuun?
word = input("Syötä sana > ")
char_counts = {}
for char in word:
  char = char.lower()
  if char not in char_counts:
    char_counts[char] = 0
  char_counts[char] += 1

print(char_counts)
