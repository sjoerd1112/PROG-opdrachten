def standaardprijs(afstandKM):
    if afstandKM <= 50 and afstandKM > 0:
        prijs = afstandKM * 0.8         #korte rit
    elif afstandKM > 50:
        prijs = afstandKM * 0.6 + 15    #lange rit
    if afstandKM < 0:
        prijs = 0                       #negatieve afstand
    return prijs

def ritprijs(leeftijd, weekendrit, afstandKM):
    prijs = standaardprijs(afstandKM)
    if leeftijd < 12 or leeftijd >= 65:
        if weekendrit == True:
            prijs = prijs*0.65        #in het weekend, jonger dan 12 of 65 of ouder
        elif weekendrit == False:
            prijs = prijs*0.7         #niet in het weekend, jonger dan 12 of 65 of ouder
    else:
        if weekendrit == True:
            prijs = prijs*0.6         #in het weekend, tussen 12 en 65
        else:
            prijs = prijs              #niet in het weekend, tussen 12 en 65
    return round(prijs,2)


afstandKM = int(input("Wat is de afstand: "))
weekendrit = input("Weekendrit, False/True: ")
leeftijd = int(input("Hoe oud ben je: "))

print("De ritprijs is €" + str((ritprijs(leeftijd, weekendrit, afstandKM))))
