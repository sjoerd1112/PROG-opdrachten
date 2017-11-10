zin = input("Voer een zin in: ")

def gemiddelde(zin):
    woord = zin.split(" ")
    i = 0
    totale_lengte = 0
    for lengte in woord:
        totale_lengte += len(lengte)
        i += 1
    gemiddeld = round(totale_lengte/i,1)
    print("De gemiddelde lengte van een woord in deze zin is", gemiddeld, "letters lang.")

gemiddelde(zin)