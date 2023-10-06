aantalcroissanten = int(input("Hoeveel croissantjes wil je? "))
aantalstokbroodjes = int(input("Hoeveel stokbroden wil je? "))
aantalkortingsbonnetjes = int(input("Hoeveel geldige kortingsbonnetjes heb je? "))

CROISSANT = 39  
STOKBROOD = 278 
KORTINGSBON = 50  

aantalcroissantenkosten = CROISSANT * aantalcroissanten
aantalstokbroodkosten = STOKBROOD * aantalstokbroodjes
aantalkortingsbonnetjeskorting = KORTINGSBON * aantalkortingsbonnetjes
totaal = aantalcroissantenkosten + aantalstokbroodkosten
totaalkorting = totaal - aantalkortingsbonnetjeskorting

print(f"De feestlunch kost je bij de bakker {totaalkorting} cent voor de {aantalcroissanten} croissantjes en de {aantalstokbroodjes} stokbroden als de {aantalkortingsbonnetjes} kortingsbonnen nog geldig zijn")
