a = int(input("noem getal A op: "))
b = int(input("noem getal B op: "))

if a > b:
	max = a
	print(f"A is het grootste getal: {max}")

elif b > a:
	max = b
	print(f"B is het grootste getal: {max}")

else:
	print("a en b zijn gelijk, er is geen grootste getal.")