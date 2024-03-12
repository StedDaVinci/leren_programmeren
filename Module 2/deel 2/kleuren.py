import random
kleuren = ("oranje", "blauw", "groen", "bruin")
zak = {
  "oranje": 0,
  "blauw": 0,
  "groen": 0,
  "bruin": 0
}

def kleuren_kiezen():
	hoeveel_m = int(input("hoeveel M&M's wil je in de zak toevoegen: "))
	for i in range(hoeveel_m):
		rndm_kleur = random.choice(kleuren)
		zak[rndm_kleur] += 1
	print(f"de inhoud van de zak: {zak}")


kleuren_kiezen()