stations = ["Schagen","Heerhugowaard","Alkmaar","Castricum","Zaandam","Amsterdam Sloterdijk","Amsterdam Centraal","Amsterdam Amstel","Utrecht Centraal","'s-Hertogenbosch","Eindhoven","Weert","Roermond","Sittard","Maastricht"]
def inlezen_beginstation(stations):
    while True:
        beginstation = str(input("Wat is uw beginstation: "))
        if beginstation in stations:
            return beginstation
            break

        else:
            print("Deze trein komt niet in", beginstation)

def inlezen_eindstation(stations):
    while True:
        eindstation = str(input("Wat is uw eindstation: "))
        if eindstation in stations:
            return eindstation
            break
        else:
            print("Deze trein komt niet in", eindstation)

def omroepen_reis(stations,beginstation,eindstation):
    i = 0
    for begin in stations:
        if beginstation == stations[i]:
            print("Het beginstation", beginstation, "heeft stationnummer", i+1, "in het traject")
            break
        else:
            i+=1
    p = 0
    for eind in stations:
        if eindstation == stations[p]:
            print("Het eindstation", eindstation, "heeft stationnummer", p+1 , "in het traject")
            break
        else:
            p+=1
    print("De afstand bedraagt", p-i, "station(s)")
    print("De prijs van het kaartje is", ((p-i)*5), "euro")


beginstation = inlezen_beginstation(stations)
eindstation = inlezen_eindstation(stations)
omroepen_reis(stations,beginstation,eindstation)
