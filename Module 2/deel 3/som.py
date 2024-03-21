som = 50
vijftig = 51
toevoeging = 1
hoeveel_toevoeging = -1
getallen = []

while som <= 1000:
	som += vijftig
	hoeveel_toevoeging += toevoeging
	getallen.append(f" + {vijftig + hoeveel_toevoeging}")
	print(f"50{''.join(getallen)} = {som}")
	vijftig += toevoeging
