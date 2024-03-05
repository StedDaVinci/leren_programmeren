import time

for i in range(1,13):
	if i <= 12:
		print(f"{i} AM")
	else:
		print(f"{i} PM")
	time.sleep(1)