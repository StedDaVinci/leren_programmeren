rum = input("zit er Rum in je Cocktail (j/n): ").lower()

if rum == "j":
	welke_rum = input("zit er Rum of Dark Rum in je cocktail: ").lower()

	if welke_rum == "dark rum":
		print("De cocktail die je drinkt is de: Dark 'n stormy | € 9,95")
	
	elif welke_rum == "rum":
		sprite = input("zit er sprite in je cocktail (j/n): ").lower()
		if sprite == "j":
			print("De cocktail die je drinkt is de: Mojito | € 9,95")
	
	elif welke_rum == "rum":
		lime_juice = input("zit er lime juice in je cocktail (j/n): ").lower()
		if lime_juice == "j":
			print("De cocktail die je drinkt is de: Strawberry daquiri | € 11,25")
	
	elif welke_rum == "rum":
		rum_vodka = input("zit er vodka in je cocktail (j/n): ").lower
		if rum_vodka == "j":
			print("De cocktail die je drinkt is de: Long island iced tea | € 11,25")
	
	else:
		pinapple_juice = input("zit er pineapple juice in je cocktail (j/n): ").lower()
		if pinapple_juice == "j":
			soda_water = input("zit er soda water in je cocktail (j/n): ").lower()
			if soda_water == "j":
				print("De cocktail die je drinkt is de: Hawaiian island | € 9,95")
			else:
				print("De cocktail die je drinkt is de: Piña colada | € 9,95")

else:
	vodka = input("zit er Vodka in je Cocktail (j/n): ").lower()

	if vodka == "j":
			orange_juice = input("zit er orange juice in je cocktail (j/n): ")
			if orange_juice == "j":
				peach_liquer = input("zit er peach liquer in je cocktail (j/n): ")
				if peach_liquer == "j":
					print("De cocktail die je drinkt is de: Sex on the beach | € 9,95")
				else:
					grenadine = input("zit er grenadine in je cocktail (j/n): ")
					if grenadine == "j":
						print("De cocktail die je drinkt is de: Bora bora | € 9,95")
					else:
						pisang_ambong = input("zit er pisang ambong in je cocktail (j/n): ")
						if pisang_ambong == "j":
							print("De cocktail die je drinkt is de: The hulk | € 9,95")
						else:
							print("je hebt een onbekende cocktail")
		
			else:
				passoa = input("zit er passoa in je cocktail (j/n): ")
				if passoa == "j":
					print("De cocktail die je drinkt is de: pornstar martini | € 11,25")
				else:
					print("De cocktail die je drinkt is de: Moscow mule | € 9,95")
	else:
		print("onbekende cocktail")