# Pizza Afmeting
PAs = 25
PAm = 30
PAl = 35

# Pizza Prijs
PSs = 12.49
PSm = 15.49
PSl = 17.49

# Pizza Kost
PKs = 0
PKm = 0
PKl = 0

while True:
	WelkePizza = input("welke maat pizza wil je bestellen? (Small/Medium/Large)").lower()
	if WelkePizza == "small" or WelkePizza == "medium" or WelkePizza == "large":
		while True:
			try:
				hvlpizza = int(input(f"hoeveel {WelkePizza} pizza's wil je bestellen?"))
				break
			except ValueError:
				print("Vul een getal in")

		if WelkePizza == "small":
			PKs += (PSs * hvlpizza)

		elif WelkePizza == "medium":
			PKm += (PSm * hvlpizza)

		elif WelkePizza == "large":
			PKl += (PSl * hvlpizza)

	else:
		print("Deze pizza is onbekend")
		
		continue

	eindBesteling = input("Wil je betalen of wil je nog verder kiezen? (Betalen/Verder)").lower()

	if eindBesteling != "verder":
		break

if PKs > 0:
	print(f"je order bevat {PKs / PSs, 2} Small pizza('s) en kost €{round(PKs, 2)}")
if PKm > 0:
	print(f"je order bevat {PKm / PSm, 2} Medium pizza('s) en kost €{round(PKm, 2)}")
if PKl > 0:
	print(f"je order bevat {PKl / PSl, 2} Large pizza('s) en kost €{round(PKl, 2)}")

print(f"de totale kosten van je bestelling kost €{round(PKs + PKm + PKl, 2)}")