# Set alustetaan {} syntaksilla. Set on järjestämätön tietorakenne, eli sen sisällön järjestys
# voi muuttua aina, kun sinne lisätään tai poistetaan dataa
units = {"tank", "plane", "ship", "dog"}
print(units)

# Set:iin voi lisätä dataa add-funktiolla
units.add("soldier")
print(units)

# Set ei salli duplikaattiarvoja
units.add("dog")
print(units)

unitList = ["tank", "plane", "ship", "dog", "dog", "dog"]
print (unitList)
# Muunnetaan lista set:ksi ja takaisin listaksi. Tämä poistaa duplikaatit (koska set ei tue niitä).
# Sivuvaikutuksena listan järjestys muuttuu
unitList = list(set(unitList))
print(unitList)

# Set:iin voi lisätä kerralla useamman alkion
units.update(["heavy tank", "helicopter"])
print(units)

# Discard ja remove poistavat alkion set:stä. Ero näiden välillä on, että jos alkio ei ole set:n
# jäsen, discard ei tee silloin mitään, mutta remove nostaa virheen, joka kaataa sovelluksen, jos
# sitä ei käsitellä.
units.discard("dog")
units.discard("dog")
print(units)

# units.remove("dog")
print(units)

# Myös pop toimii set:lle
random = units.pop()
print(random)

print(units)