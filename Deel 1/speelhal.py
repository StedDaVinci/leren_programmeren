groepgrootte = 4
tickets = 7.45
vrper5min = 0.37
lengtevr = 45
per5min = 5

hoelangvr = lengtevr / per5min
kostentickets = groepgrootte * tickets
perpersoonvr = vrper5min * hoelangvr
totaalvrkosten = perpersoonvr * groepgrootte
allestotaal = round(totaalvrkosten + kostentickets)

print(f"de totale kosten voor de vr is {totaalvrkosten} euro, de tickets kosten intotaal {kostentickets} euro en intotaal is alles {allestotaal} euro.")