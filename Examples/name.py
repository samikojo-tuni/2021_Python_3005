# Harjoitus
# Kirjoita ohjelma, joka kysyy käyttäjän nimeä. Ohjelma tulostaa esim. tekstin
# "Mikä sinun nimesi on?" nimeä kysyttäessä.
# Jos nimi on kirjoitettu pienellä alkukirjaimella, ohjelma muuttaa nimen alkukirjaimen
# isolla kirjoitetuksi. Lopuksi ohjelma tulostaa "Sinun nimesi on <Nimi>"
name = input("What is your name? ")
print("Your name is " + name.capitalize())