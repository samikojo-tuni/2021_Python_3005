a = 30  # Arvon sijoitus muuttujaan
b = 20

# Vertailuoperaattoreita
# == yhtäsuuruusvertailu

if a == b:  # Onko a yhtä suuri kuin b
    print(a, "equals", b)
else:
    # sep-parametrilla voidaan määrittää print-funktion käyttämä erotinmerkki
    print(a, "does not equal", b)

# != Erisuuruusvertailu
if a != b:
    print(a, "does not equal", b)
else:
    print(a, "equals", b)

if not a == b:
    print(a, "does not equal", b)
else:
    print(a, "equals", b)

# < pienempi kuin, > suurempi kuin
if a < b:
    print(a, "is less than", b)
elif a > b:
    print(a, "is greater than", b)
else:
    print(a, "equals", b)

# <= pienempi tai yhtä suuri kuin, >= suurempi tai yhtä suuri kuin
if a <= b:
    print(a, "is less than or equals", b)
else:
    print(a, "is greater than", b)

# Vertailun tulos voidaan tallentaa muuttujaan
result = a == b
print(result)

if result:
    print(a, "equals", b)
else:
    print(a, "does not equal", b)

if not result:
    print(a, "does not equal", b)
else:
    print(a, "equals", b)

# Python ei tue Switch-case rakennetta
