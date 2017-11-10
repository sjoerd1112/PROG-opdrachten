import datetime
import csv
bestand = 'logins.csv'
while True:
    csvfile = open(bestand, 'a',newline='')
    file = csv.writer(csvfile, delimiter=';')
    naam = input("Wat is je achternaam? ")
    voorl = input("Wat zijn je voorletters? ")
    gbdatum = input("Wat is je geboortedatum? ")
    email = input("Wat is je e-mail adres? ")
    file.writerow((voorl, naam, gbdatum, email))
    csvfile.close()