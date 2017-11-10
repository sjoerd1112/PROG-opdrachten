lijst = str(input("Geef lijst met minimaal 10 strings: "))
lijst2 = []

woorden = lijst.split(" ")

for woord in woorden:
    if len(woord) == 4:
        lijst2.append(woord)
print('De nieuw gemaakte lijst met 4-letterige woorden is: ' + str(lijst2))
