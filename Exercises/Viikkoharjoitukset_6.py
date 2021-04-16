'''
Tehtävä 1:

Kirjoita funktio, joka ottaa parametrinaan vuosiluvun ja palauttaa True tai False sen perusteella,
onko vuosi karkausvuosi. Karkausvuosia ovat neljällä jaolliset vuodet. Poikkeuksena tähän on sadalla
jaolliset vuodet. Niiden pitää olla jaollisia myös 400 ollakseen karkausvuosia.
'''

'''
Tehtävä 2:

Kirjoita luokka Time, joka ottaa rakentajan parametrina ajan tunteina, minuutteina ja sekunteina.
Älä käytä apuna aika- tai matematiikkakirjastoja!

Luokassa on seuraavat jäsenfunktiot:
- Hours()
  - palauttaa ajan tuntiosan
- Minutes()
  - palauttaa ajan minuuttiosan
- Seconds()
  - palauttaa ajan sekuntiosan
- TotalHours()
  - palauttaa kokonaisajan tunteina kokonaislukuna
- TotalMinutes()
  - palauttaa kokonaisajan minuutteina kokonaislukuna
- TotalSeconds()
  - palauttaa kokonaisajan sekunteina kokonaislukuna
- ToString()
  - palauttaa ajan muodossa hh:mm:ss

Esimerkki:
aika = Time(12,35,0)
aika.ToString()     # Palauttaa 12:35:00 (Huomaa etunollat)
aika.Hours()        # Palauttaa 12
aika.Minutes()      # Palauttaa 35
aika.Seconds()      # Palauttaa 0
aika.TotalHours()   # Palauttaa 12
aika.TotalMinutes() # Palauttaa 755
aika.TotalSeconds() # Palauttaa 45 300
'''
