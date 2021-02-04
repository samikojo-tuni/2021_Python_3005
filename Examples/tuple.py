phones = ("Nokia", "Apple", "Samsung")

print(phones)

# Palauttaa tuplesta alkion indeksistä 1 ja tallentaa sen muuttujaan phone
phone = phones[1]
print(phone)

# Alkion poisto ei onnistu, koska tuple on muuttamaton tietorakenne
# del phones[1]
print(phones)

# Koko tuplen poisto on kuitenkin sallittua
# del phones

# print(phones)

phoneList = list(phones)
phoneList.append("OnePlus")
phones = tuple(phoneList)

print(phones)
