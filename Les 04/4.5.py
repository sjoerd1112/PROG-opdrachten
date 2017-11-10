def kwadraten_som(grondgetallen):
    som = 0
    for getal in grondgetallen:
        if getal > 0:
            kwadraat = getal * getal
            som += kwadraat
    return som


grondgetallen = [4,5,3,-81]
print(kwadraten_som(grondgetallen))
