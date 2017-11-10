def lang_genoeg(lengte):
    if lengte > 119:
        print("Je bent lang genoeg voor de attractie!")
    else:
        print("Je bent te klein!")

lengte = eval(input("Voer je lengte in in centimeters: "))
lang_genoeg(lengte)
