#!/usr/bin/python3

import cgi
import cgitb
import os
# TODO: Lisää tarvittavat moduulit

# Poista tämä rivi, kun sovellus on valmis. Tuotantokäytössä emme halua koskaan paljastaa koodissa
# potentiaalisesti olevia bugeja.
cgitb.enable()

# Pisteet lähetetään sovellukselle JSON-muodossa. Tämä pitää kommunikoida sovellukselle.
print("Content-type: application/json\n\n")

# HTTP-metodin selvitys
cgi_method = os.environ["REQUEST_METHOD"]
if cgi_method == "POST":
  # Pisteiden lisäys
  # TODO: Toteuta minut!
  print("Lisätään pisteet")
else:
  # Pisteiden lähetys sovellukselle
  # TODO: Toteuta minut!
  print("Näytä pisteet")
