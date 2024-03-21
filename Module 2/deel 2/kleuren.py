import random
kleuren = ("oranje", "blauw", "groen", "bruin")
zak = {

}

def kleuren_kiezen():
	hoeveel_m = int(input("hoeveel M&M's wil je in de zak toevoegen: "))
	for _ in range(hoeveel_m):
		rndm_kleur = random.choice(kleuren)
		if rndm_kleur not in zak:
			zak[rndm_kleur] = 0
		zak[rndm_kleur] += 1
	print(f"de inhoud van de zak: {zak}")


kleuren_kiezen()