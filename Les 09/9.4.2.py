import csv

bestand = 'producten.csv'

csvfile = open(bestand, 'r',newline='')
file = csv.reader(csvfile, delimiter=';')

firstRow = True
duurste = 0
voorraad = -1
duurste_id = 0
vorraad_id = 0
teller = 0
artikelen = []
totaal_voorraad = 0

for regel in file:
    if firstRow:
        firstRow = False
    else:
        if float(regel[4]) > duurste:
            duurste = float(regel[4])
            duurst_id = teller

        if float(regel[3]) < voorraad or voorraad==-1:
            voorraad = float(regel[3])
            vorraad_id = teller

        artikelen.append(regel)
        totaal_voorraad+=int(regel[3])
        teller +=1

print("Het duurste artikel is {} en kost {} Euro.".format(artikelen[duurste_id][2],duurste))
print("Er zijn {} artikelen in voorraad van het productnummer {}.".format(voorraad,artikelen[vorraad_id][0]))
print("In totaal liggen er {} producten in ons magazijn.".format(totaal_voorraad))

csvfile.close()