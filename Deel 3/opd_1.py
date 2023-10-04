a = int(input("noem getal A op: "))
b = int(input("noem getal B op: "))

if a > b:
	max = a
	min = b
	print(f"A is het grootste getal: {max}")
	print(f'Het minimum is: {min}')
	print(f'Het maximum is: {max}')

elif b > a:
	min = a
	max = b
	print(f"A is het kleinste getal: {min}")
	print(f'Het minimum is: {min}')
	print(f'Het maximum is: {max}')

else:
	print("a en b zijn even groot")