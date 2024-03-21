aantal_vragen = 0

while True:	
	vraag = input('? ')
	aantal_vragen += 1
	if vraag == 'quit':
		print(aantal_vragen)
		break
	else:
		continue

