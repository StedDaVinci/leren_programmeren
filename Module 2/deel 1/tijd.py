import time

for AM in range(1,13):
	print(f"{AM} AM")
	time.sleep(1)
	if AM == 12:
		for PM in range(1,13):
			print(f"{PM} PM")
			time.sleep(1)
	
	

