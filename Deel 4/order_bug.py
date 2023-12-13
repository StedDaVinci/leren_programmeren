def vraag_getal(aantal):
    antwoord = input(f"Voer het {antwoord} getal in: ")
    getal = int(aantal)
    return getal

getal_1 = vraag_getal("eerste")
getal_2 = vraag_getal("tweede")

def deel_getallen(a, b):
    antwoord = print(a / b)
    return antwoord

resultaat = deel_getallen(getal_1, getal_2)

if getal_2 == 0:
    print("Kan niet delen door 0")
else:
    print (f"{getal_1} gedeeld door {getal_2} is gelijk aan {resultaat}".format(getal_1, getal_2, resultaat))