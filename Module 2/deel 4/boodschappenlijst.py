lijst = {

}

while True:
	artikel = input("Welke artikel wilt u toevoegen? ")
	aantal = int(input(f"Hoeveel {artikel} wilt u toevoegen? "))
	if artikel not in lijst:
		lijst[artikel] = 0
	lijst[artikel] += aantal
	artikel_toevoegen = input("wilt u nog een artikel toevoegen? (ja/nee)").lower()
	if artikel_toevoegen == "nee":
		break

print("-[ Boodschappenlijst ]-")
print()
for item, hoeveelheid in lijst.items():
	print(f"{hoeveelheid}x {item}")
print()
print("-----------------------")