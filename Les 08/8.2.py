import random
dubbel = 0
worp1 = random.randrange(1,7)
worp2 = random.randrange(1,7)
if worp1 == worp2:
    print(worp1, "+", worp2, "=", worp1+worp2, "(dubbel)")
    worp1 = random.randrange(1,7)
    worp2 = random.randrange(1,7)
    if worp1 == worp2:
        print(worp1, "+", worp2, "=", worp1 + worp2, "(dubbel)")
        worp1 = random.randrange(1, 7)
        worp2 = random.randrange(1, 7)
        if worp1 == worp2:
            print(worp1, "+", worp2, "=", worp1 + worp2, "(direct naar de gevangenis)")
        else:
            print(worp1, "+", worp2, "=", worp1 + worp2)
    else:
        print(worp1, "+", worp2, "=", worp1 + worp2)
else:
    print(worp1, "+", worp2, "=", worp1+worp2)
