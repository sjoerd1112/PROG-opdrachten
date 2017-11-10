infile = open("kaartnummers.txt", "r")
grootste_nummer,line_nummer,regels = 0,0,0
for line in infile.readlines():
    lines = line.split(',')
    regels += 1
    if int(lines[0]) > grootste_nummer:
        grootste_nummer = int(lines[0])
        line_nummer = regels
print("Deze file telt {} regels" .format(regels))
print("Het grootste kaartnummer is: {} en staat op regel {}" .format(grootste_nummer,line_nummer))
infile.close()
