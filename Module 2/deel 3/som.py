som = 50
optellend_getal = 51
getallen = []

while som <= 1000:
	som += optellend_getal
	getallen.append(f" + {optellend_getal}")
	print(f"50{''.join(getallen)} = {som}")
	optellend_getal += 1