Lijstje_hoeveelheid = int(input("hoeveel lijstjes wil je?: "))

lijst = []
for x in range(1,Lijstje_hoeveelheid + 1):
	hoeveel_in_lijstje = int(input(f"hoeveel in lijstje {x}? "))
	tijdelijke_lijst = []
	for y in range(hoeveel_in_lijstje):
		tijdelijke_lijst.append((y + 1) * x)
	lijst.append(tijdelijke_lijst)

print(lijst)