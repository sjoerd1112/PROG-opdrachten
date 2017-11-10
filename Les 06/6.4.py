studentencijfers = [ [95, 92, 86],[66, 75, 54],[89, 72, 100],[34, 0, 0]]
def gemiddelde_per_student(studentencijfers):
    for getal in range (len(studentencijfers)):
        totaal = 0
        for nummer in studentencijfers[getal]:
            totaal += nummer
            gemiddelde = totaal / len(studentencijfers[0])
        return gemiddelde

def gemiddelde_van_alle_studenten(studentencijfers):
    som = 0
    lengte = 0
    for number in range (len(studentencijfers)):
        for getallen in studentencijfers[number]:
            lengte += 1
            som += getallen
    totaalgemiddelde = som / lengte
    return (totaalgemiddelde)

print(gemiddelde_per_student(studentencijfers))
print(round(gemiddelde_van_alle_studenten(studentencijfers),1))
