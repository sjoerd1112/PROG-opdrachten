invoer = "5-9-7-1-7-8-3-2-4-8-7-9"
getallenlijst = []
getallen = invoer.split("-")
for getal in getallen:
    intgetal = int(getal)
    getallenlijst.append(intgetal)
getallenlijst.sort()
grootste = 0
kleinste = 9999999
for grootklein in getallenlijst:
    if grootklein > grootste:
        grootste = grootklein
    if grootklein < kleinste:
        kleinste = grootklein
aantal = 0
for numbers in getallenlijst:
    aantal += 1
som = 0
for number in getallenlijst:
    som += number

gemiddelde = som / len(getallenlijst)

print("Gesorteerde list van ints: {}".format(getallenlijst))
print("Het kleinste getal is {} en het grooste getal is {}".format(kleinste,grootste))
print("Het aantal getallen is {} en de som van de getallen is {}".format(aantal,som))
print("Gemiddelde =", round(gemiddelde,2))
