maandnummer = int(input("welke maand is het (getal): "))

def seizoen(maandnummer):
    if maandnummer in [12,1,2]:
        print("winter")
    elif maandnummer in [3,4,5]:
        print("lente")
    elif maandnummer in [6,7,8]:
        print("zomer")
    elif maandnummer in [9,10,11]:
        print("herfst")

(seizoen(maandnummer))
