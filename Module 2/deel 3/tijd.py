import time

for uur in range(1,25):
	if uur <= 11:
		if uur <= 9:
			print(f"{0}{uur} AM")
		else:
			print(f"{uur} AM")
	elif uur == 12:
		print(f"{uur} PM")
		# 12 pm
	
	elif uur >= 13 and uur <= 23:
		if uur - 12 <= 9:
			print(f"{0}{uur - 12} PM")
		else:
			print(f"{uur - 12} PM")
		# 1 tot 11 pm
	else:
		# 12 am
		print(f"{uur - 12} AM")
	time.sleep(0.5)
	
	

