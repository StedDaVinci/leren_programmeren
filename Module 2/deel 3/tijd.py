import time

for uur in range(1,25):
	if uur <= 12:
		if uur <= 9:
			print(f"{0}{uur} AM")
		else:
			print(f"{uur} AM")
	else:
		if uur - 12 <= 9:
			print(f"{0}{uur - 12} PM")
		else:
			print(f"{uur - 12} PM")
	time.sleep(1)
	
	

