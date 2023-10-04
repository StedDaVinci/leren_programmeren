aantalcroissanten = int(input("Hoeveel croissantjes wil je? "))
aantalstokbroodjes = int(input("Hoeveel stokbroden wil je? "))
aantalkortingsbonnetjes = int(input("Hoeveel geldige kortingsbonnetjes heb je? "))

croissant = 39  
stokbrood = 278 
kortingsbon = 50  

aantalcroissantenkosten = croissant * aantalcroissanten
aantalstokbroodkosten = stokbrood * aantalstokbroodjes
aantalkortingsbonnetjeskorting = kortingsbon * aantalkortingsbonnetjes
totaal = aantalcroissantenkosten + aantalstokbroodkosten
totaalkorting = totaal - aantalkortingsbonnetjeskorting

print(f"De feestlunch kost je bij de bakker {totaalkorting} cent voor de {aantalcroissanten} croissantjes en de {aantalstokbroodjes} stokbroden als de {aantalkortingsbonnetjes} kortingsbonnen nog geldig zijn")
