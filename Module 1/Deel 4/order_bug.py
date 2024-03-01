def vraag_getal(aantal):
    vraag = int(input(f"Voer het {aantal} getal in: "))
    getal = int(vraag)
    return getal

def deel_getallen(a, b):
    antwoord = a / b
    return antwoord

getal_1 = vraag_getal("eerste")
getal_2 = vraag_getal("tweede")

if getal_2 == 0:
    print("Kan niet delen door 0")

else:
    resultaat = deel_getallen(getal_1, getal_2)
    print (f"{getal_1} gedeeld door {getal_2} is gelijk aan {resultaat}".format(getal_1, getal_2, resultaat))