def code(invoer):
    output = ''
    for letter in invoer:
        letter = ord(letter)
        letter +=3
        letter = chr(letter)
        uitvoer = output + letter
    print(output)

code("RutteAlkmaarDen Helder")
