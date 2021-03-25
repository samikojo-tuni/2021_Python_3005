import json

def main():
  data = []

  brandKey = "brand"
  modelKey = "model"
  yearKey = "year"
  priceKey = "price"
  colorKey = "color"

  carInfo = {
    brandKey: "Toyota",
    modelKey: "Corolla",
    yearKey: 2010,
    priceKey: 6502.15
  }

  carInfo2 = {
    brandKey: "Ford",
    modelKey: "Focus",
    yearKey: 2000,
    priceKey: 1500.00
  }

  data.append(carInfo)
  data.append(carInfo2)

  jsonData = json.dumps(data, indent=2)

  file = open("cars.json", "w", encoding="utf-8")
  file.write(jsonData)
  file.close()

  print(jsonData)


if __name__ == "__main__":
  main()
