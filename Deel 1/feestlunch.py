croissant = 0.39
stokbrood = 2.78
kortingsbon = 0.5

aantalcroissantenkosten = croissant * 17
aantalstokbroodkosten = stokbrood * 2
aantalkortingsbonnetjes = kortingsbon * 3
totaal = aantalcroissantenkosten + aantalstokbroodkosten
totaalkorting = totaal - aantalkortingsbonnetjes

print(f"het kost intotaal {totaalkorting} met kortingsbonnetjes")
