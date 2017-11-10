studenten = dict()
studenten["Rick"]=5.5
studenten["Tom"]=7.6
studenten["Daan"]=9.3
studenten["Tristan"]=1.5
studenten["David"]=9.7
studenten["Erik"]=6.9
studenten["Thomas"]=7.2
studenten["Dennis"]=9.1

for nummer in studenten:
    if studenten[nummer] > 9:
        print(nummer,"heeft een",studenten[nummer], "gehaald!")
