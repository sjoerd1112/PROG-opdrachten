def convert(celcius):
    fahr = celcius * 1.8 + 32
    print("{:4}   {:4}".format(round(fahr),celcius))
def table():
    print("{:4}   {:4}".format("F","C"))
    for i in range(-30,50,10):
        convert(i)
table()