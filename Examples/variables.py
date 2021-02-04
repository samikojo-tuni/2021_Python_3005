# Muuttujien määrittäminen. Python tulkki osaa päätellä tyypin muuttujan arvosta
muuttuja1 = 1 # Integer
muuttuja2 = "Tekstiä" # String

print(muuttuja1)

# Python on dynaamisesti tyypitetty kieli
# Muuttujan tyyppi päätellään ajon aikana, kun muuttujan alustava rivi suoritetaan
# Muuttujan tyypin pystyy muuttamaan määrittämällä muuttuja uudelleen
muuttuja1 = "Tekstiä" # Muuttujan tyyppi muuttui integeristä stringiksi

print(muuttuja1)

muuttuja1 = 1 # Integer, kokonaisluku
muuttuja2 = "Tekstiä" # String, merkkijono
muuttuja3 = 1.2 # Float, desimaaliluku
muuttuja4 = True # Boolean, totuusarvo (True tai False)

numero1 = 2
numero2 = 4

tulos = 0

# Yhteenlasku
tulos = numero1 + numero2

print(tulos)

# Vähentää tulos-muuttujasta muuttujan numero1 arvon
# ja tallentaa tuloksen tulos-muuttujaan
# tulos = tulos - numero1
tulos -= numero1

# Jakolasku
# Tulos float-tyyppiä vaikka molemmat jaettava ja jakava ovat kokonaislukuja
tulos = numero1 / numero2
print(tulos)

# Jakolasku, joka palauttaa kokonaisluvun
tulos = numero1 // numero2
print(tulos)

# Vastaavasti
# += Lisäys ja sijoitus
# -= Vähennys ja sijoitus
# *= Kertolasku ja sijoitus
# /= Jakolasku ja sijoitus
# //= Kokonaislukujen jakolasku ja sijoitus

# Python on vahvasti tyypitetty kieli
muuttuja1 = 10
muuttuja2 = "Tekstiä"

# Esimerkiksi eri tyyppisten muuttujien ei ole mahdollista
# print(muuttuja2 + muuttuja1)

# Koodaajan vastuulla on suorittaa tyyppimuunnos
# Esim. alla oleva koodi muuttaa kokonaisluvun string:ksi, jonka jälkeen lisäys toimii
print(muuttuja2 + str(muuttuja1))

# Lainausmerkit
print("Tulostuuko tämä?")
print('Tämä on vastaava merkkijono')
print('Tämä on "lainaus"') # Lainausmerkkien käyttö merkkijonon sisällä
print("Tämä on \"lainaus\"") # Lainausmerkit voidaan merkitä kenoviivalla, jolloin
# se tulkitaan kuuluvan osaksi merkkijonoa
# print("Tämä ei toimi') # Tällä tavoin lainausmerkkejä ei voi yhdistää

# Pitkät tekstit pitää katkaista rivinvaihtomerkillä \, mikäli haluamme rivittää sen
# usealle riville (muuten Python tulkitsee koodirivin päättyneeksi)
print("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor \
incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud \
exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure\
 dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.\
 Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt\
 mollit anim id est laborum.")

 # """ määrittää usean rivin merkkijonon. Kaikki merkit """ lainauksen sisällä tulkitaan
 # kuuluvan osaksi merkkijonoa

longText = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit, sed do
eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim
veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum
dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident,
sunt in culpa qui officia deserunt mollit anim id est laborum."""

print(longText)

# Usean rivin kommenttina Pythonissa voidaan käyttää """ operaattoria
""" Tämä
on 
usean rivin
kommentti """

print("Yllä oleva toimii kommenttina")

# Tyyppimuunnoksia
# int(muuttuja) muuttaa muuttujan integeriksi
# float(muuttuja) muuttaa muuttujan desimaaliluvuksi
# str(muuttuja) muuttaa muuttujan stringiksi

# Boolean eli totuusarvo
# Arvo 0 (int, float, tyhjä string ("")) vastaa totuusarvoa False, mikä tahansa nollasta poikkeava
# vastaa totuusarvoa True
print(bool(-1))