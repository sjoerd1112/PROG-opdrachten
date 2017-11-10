def namen():
    lijst = dict()

    while True:
        naam = input("Volgende naam: ")
        if (naam == ""):
            break

        if (lijst.get(naam) != None):
            lijst[naam] += 1
        else:
            lijst.setdefault(naam, 1)

    for key in lijst:
        if lijst[key] == 1:
            print("Er is 1 student met de naam", key)
        else:
            print("Er zijn", lijst[key], "studenten met de naam", key)

namen()