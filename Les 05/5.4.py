import datetime

while True:
    file = open('hardlopers.txt', 'a')
    naam = input("Naam van de hardloper: ")
    vandaag = datetime.datetime.today()
    s = vandaag.strftime("%a %d %b %Y %H:%M:%S")
    file2 = s + ", " + naam + '\n'
    file.write(file2)
    file.flush()
    file.close()
    print(s, ",", naam)