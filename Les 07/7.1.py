i = 0
som = 0
getal = 1
while getal != 0:
    getal = float(input("Geef een getal: "))
    i += 1
    som+=getal
print("Er zijn", i-1, "getallen ingevoerd, de som is: ", float(som))