def ticker(filename):
    infile = open(filename, "r")
    inhoud = infile.readlines()
    infile.close()
    lijst = dict()
    for regel in inhoud:
        regel = regel[:-1]
        lijst[regel.split(":")[0]] = regel.split(":")[1]
    return lijst
print(ticker("ticker.txt"))
