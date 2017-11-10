kosten = 4356
aantal = 0

try:
    aantal = int(input("Vul aantal mensen in: "))
except:
    print("Gebruik cijfers voor het invoeren van het aantal!")
    exit()

if(aantal == 0):
    print("Delen door nul kan niet!")
    exit()
elif(aantal < 0):
    print("Negatieve getallen zijn niet toegestaan!")
    exit()

try:
    kosten_per_persoon = kosten / aantal
    print("De kosten per persoon zijn €",kosten_per_persoon)
except:
    print("Onjuiste invoer!")