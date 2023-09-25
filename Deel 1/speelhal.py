GROEPGROOTTE = 4
TICKETS = 7.45
VRPER5MIN = 0.37
LENGTEVR = 45
PER5MIN = 5

hoelangvr = LENGTEVR / PER5MIN
kostentickets = GROEPGROOTTE * TICKETS
perpersoonvr = VRPER5MIN * hoelangvr
totaalvrkosten = perpersoonvr * GROEPGROOTTE
allestotaal = round(totaalvrkosten + kostentickets)

print(f"de totale kosten voor de vr is {totaalvrkosten} euro, de tickets kosten intotaal {kostentickets} euro en intotaal is alles {allestotaal} euro.")