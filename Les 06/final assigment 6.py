#menu
print("1: Ik wil weten hoeveel kluizen er nog beschikbaar zijn")
print("2: Ik wil een nieuwe kluis")
print("3: Ik wil even iets uit mijn kluis halen")
kluisnummers = [1,2,3,4,5,6,7,8,9,10,11,12]

def aantal_kluizen_vrij():
    lines = 0
    infile = open("kluizen.txt", "r")
    inhoud = infile.readlines()
    infile.close()
    for line in inhoud:
        if line.strip(" "):
            lines += 1
    print("Het aantal beschikbare kluizen is", 12 - lines)

def nieuwe_kluis(kluisnummers):
    infile = open("kluizen.txt", "r")
    inhoud = infile.read()
    infile.close()
    inhoud2 = inhoud.split()
    for line in inhoud2:
        nummer = line.split(";")
        kluisnummer = int(nummer[0])
        kluisnummers.remove(kluisnummer)
    wachtwoord = str(input("voer uw wachtwoord in: "))
    file = open("kluizen.txt", "a")
    file.write(str(kluisnummers[0]))
    file.write(";" )
    file.write(str(wachtwoord))
    file.write("\n")
    file.close()
    print("Uw kluisnummer is:", kluisnummers[0])

def kluis_openen():
    testlist = []
    nummer = eval(input("Voer uw kluisnummer in: "))
    wachtwoord = str(input("Voer uw wachtwoord in: "))
    infile = open("kluizen.txt", "r")
    inhoud = infile.read()
    infile.close()
    inhoud2 = inhoud.split()
    for line in inhoud2:
        combo = line.split(";")
        testlist.append(combo)
    i = 0
    while i < (len(testlist)/2):
        if int(testlist[i][0]) == nummer:
            if wachtwoord == str(testlist[i][1]):
                print("U kunt nu iets uit uw kluisje halen")
            else:
                print("verkeerd wachtwoord/kluisnummer")
            break
        else:
            i += 1




keuze = int(input("Voor welke optie kies je: "))
if keuze < 1 or keuze > 3:
    print("Er is een ongeldige waarde ingevoerd")
if keuze == 1:
    aantal_kluizen_vrij()
if keuze == 2:
    nieuwe_kluis(kluisnummers)
if keuze == 3:
    kluis_openen()

