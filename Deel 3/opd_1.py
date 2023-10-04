a = int(input("noem getal A op: "))
b = int(input("noem getal B op: "))

if a > b:
	max = a
	print(f"A is het grootste getal: {max}")

elif b > a:
	min = a
	print(f"A is het kleinste getal: {min}")

else:
	print("a en b zijn gelijk, er is geen grootste getal.")