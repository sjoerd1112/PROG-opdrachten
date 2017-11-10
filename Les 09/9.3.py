import csv
infile = open('gamers.csv', 'r')
inhoud = csv.reader(infile, delimiter=';')
highscore = 0
for regel in inhoud:
    if int(rule[2]) > highscore:
        highscore = int(rule[2])
        name = rule[0]
        time = rule[1]
print("De hoogste score is: {} op {} behaald door {}".format(highscore,time,name))