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

# Harjoitus 4:
# Pyydä käyttäjää syöttämään sanoja, kunnes käyttäjä syöttää sanan "stop".
# Lopuksi tulosta kaikki käyttäjän syöttämät sanat (paitsi "stop").


# Harjoitus 5:
# Pyydä käyttäjää syöttämään, monenko luvun keskiarvon tämä haluaa laskea.
# Tämän jälkeen pyydä käyttäjää syöttämään näin monta lukua.
# Laske lopuksi lukujen keskiarvo ja tulosta tämä käyttäjälle
# num = int(input("Syötä numero "))


# Harjoitus 6
# Pyydä käyttäjää syöttämään sana. Laske montako kertaa eri kirjaimet esiintyvät sanassa.
# Lopuksi tulosta kirjaimet ja niiden esiintymiskerrat.
# Esimerkkitulosteet:
# Syötä sana > tietokone
# { "t": 2, "i": 1, "e": 2, "o": 1, "k": 1, "n": 1 }
# Vihje: operaattorit in ja not in
# Mietittäväksi: mikä tietorakenne sopii ratkaisuun?
