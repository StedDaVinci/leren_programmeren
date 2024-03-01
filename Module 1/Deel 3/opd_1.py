a = int(input("noem getal A op: "))
b = int(input("noem getal B op: "))

if a > b:
	Max = a
	Min = b
	print(f"A is het grootste getal: {Max}")

elif b > a:
	Min = a
	Max = b
	print(f"A is het kleinste getal: {Min}")

else:
	Min = a
	Max = b
	print("a en b zijn even groot")

print(f'Het minimum is: {Min}')
print(f'Het maximusm is: {Max}')