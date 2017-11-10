cijferICOR=int(input('cijfer voor ICOR:'))
cijferPROG=int(input('cijfer voor PROG:'))
cijferCSN=int(input('cijfer voor CSN:'))
totaal_punten = cijferCSN + cijferICOR + cijferPROG
gemiddeld = totaal_punten/3
euros = totaal_punten * 30
print('Mijn cijfers (gemiddeld een', gemiddeld, '!) leveren een beloning op van', euros, 'euro')
