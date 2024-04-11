PRIJS_COLA = 1.80
PRIJS_BIER = 2.40
PRIJS_CHAMPAGNE = 12.30

DRANKJES = ('cola', 'bier', 'champagne')
VIP_LIST = ('jeroen', 'jouke', 'rudi')

#bouw hieronder de floowchart na
bandje = ""
stempel = False
age = int(input("Hoe oud ben je? "))

if age >= 18:
	naam = input("Wat is je naam? ").lower()
	if naam in VIP_LIST and age >= 21:
		if age >= 21:
			bandje = "blauw"
		else:
			bandje = "rood"
		print(f"Je krijgt van mij een {bandje} bandje.")
	else:
		if age >= 21:
			print("Je krijgt van mij een stempel.")
			stempel = True
	
	drank = input("Wil je wat drinken? ").lower()
	if drank == "cola" and bandje:
		print("Alstublieft complimenten van het huis.")
	elif drank == "cola" and not bandje:
		print(f"Asltublieft je {drank}, dat is dan €{PRIJS_COLA}")
	elif drank == "bier" and (stempel == True or bandje == "blauw"):
		print(f"Asltublieft je {drank}, dat is dan €{PRIJS_BIER}")
	elif drank == "champange" and stempel == True:
		print("sorry alleen vips mogen champange bestellen.")
	elif drank == "champange" and stempel == False and bandje == "blauw":
		print(f"Asltublieft je {drank}, dat is dan €{PRIJS_CHAMPAGNE}")
	if age <= 20 and (drank == "bier" or drank == "champange"):
		print("Sorry je mag geen drank bestellen je bent onder de 21.")
		print(f"probeer het in {21 - age} jaar nog eens")
else:
	print("Sorry, je mag niet naar binnen.")
	print(f"probeer het in {18 - age} jaar nog eens")