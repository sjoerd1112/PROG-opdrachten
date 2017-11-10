def som(getallenlijst):
    getal = 0
    for optelling in getallenlijst:
        getal += optelling
    return getal

getallenlijst = [1,2,3,4,5]
print(som(getallenlijst))
