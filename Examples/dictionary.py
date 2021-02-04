# Dictionary sisältää avain-arvo -pareja. Avaimien on oltava yksilöllisiä. Arvoja indeksoidaan
# avaimilla.

brandKey = "brand"
modelKey = "model"
yearKey = "year"
priceKey = "price"
colorKey = "color"

allCars = []

carInfo = {
    brandKey: "Toyota",
    modelKey: "Corolla",
    yearKey: 2010,
    priceKey: 6502.15
}

allCars.append(carInfo)

allCars.append({
    brandKey: "Ford",
    modelKey: "Focus",
    yearKey: 2000,
    priceKey: 1500.00
})

print("All cars", allCars)

print(carInfo)

# Arvon lisäys dictionaryyn
carInfo[colorKey] = "red"
print(carInfo)

# Jos avain on jo olemassa, olemassa oleva arvo päivittyy
carInfo[yearKey] = 2011
print(carInfo)

# Datan tallennus muuttujaan, arvo tallentuu muuttujaan
price = carInfo[priceKey]
print(price)

# Avain-arvo -parit poistetaan pop-funktiolla. Jos avainta ei löydy, palautetaan oletusarvo, jos
# sellainen on välitetty funktiolle parametrina. Jos oletusta ei ole välitetty, Python nostaa virheen
color = carInfo.pop(colorKey)
print(color)

color = carInfo.pop(colorKey, "N/A")
print(color)

color = carInfo.pop(colorKey)
print(color)
