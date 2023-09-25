aantalcroissanten = int(input("Hoeveel croissantjes wil je? "))
aantalstokbroodjes = int(input("Hoeveel stokbroden wil je? "))
aantalkortingsbonnetjes = int(input("Hoeveel geldige kortingsbonnetjes heb je? "))

croissant = 0.39
stokbrood = 2.78
kortingsbon = 0.5

aantalcroissantenkosten = croissant * aantalcroissanten
aantalstokbroodkosten = stokbrood * aantalstokbroodjes
aantalkortingsbonnetjes = kortingsbon * aantalkortingsbonnetjes
totaal = aantalcroissantenkosten + aantalstokbroodkosten
totaalkorting = round(totaal - aantalkortingsbonnetjes)

print(f"De feestlunch kost je bij de bakker {totaalkorting} euro voor de {aantalcroissanten} croissantjes en de {aantalstokbroodjes} stokbroden als de {aantalkortingsbonnetjes} kortingsbonnen nog geldig zijn")
