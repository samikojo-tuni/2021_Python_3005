# Harjoitus 1
# Luo luokka Dice, joka määrittää nopan. Luokka ottaa rakentajan parametrina nopan sivujen määrän.
# Kirjoita nopalle funktio roll, joka palauttaa satunnaisen arvon (sivujen lukumäärän mukaan).
#
# Peri luokasta Dice luokat D6, jossa on kuusi sivua ja D20, jossa on 20 sivua.


# Harjoitus 2:
# Kirjoita luokka, joka muuntaa lukuja roomalaisiksi numeroiksi ja päinvastoin
#
# Algoritmi desimaalista roomalaiseksi:
# - Tallenna seuraavat arvot soveltuvaan tietorakenteeseen:
# 1 	I
# 4 	IV
# 5 	V
# 9 	IX
# 10 	X
# 40 	XL
# 50 	L
# 90 	XC
# 100 	C
# 400 	CD
# 500 	D
# 900 	CM
# 1000 	M
#
# - Etsi tietorakenteesta suurin luku, joka on pienempi
#   tai yhtä suuri kuin muunnettava luku. Ota lukua vastaava
#   roomalainen numero talteen ja vähennä muunnettavasta
#   luvusta roomalaista numeroa vastaava arvo
# - Toista tämä, kunnes muunnettava luku on 0
#
# Algoritmi roomalaisesta desimaaliksi:
# - Mieti tätä varten vastaava tietorakenne kuin yllä.
# - Tutki, onko roomalaisen numeron 2 ensimmäistä merkkiä tunnettu
#   roomalainen numero
#   - Jos on, lisää tulokseen merkkiä vastaava desimaalinumero ja
#     siirry roomalaisessa numerossa kaksi merkkiä eteenpäin
#   - Jos ei ole, lisää vain yhtä merkkiä vastaava numero tulokseen
#     ja siirry roomalaisessa numerossa yksi merkki eteenpäin
