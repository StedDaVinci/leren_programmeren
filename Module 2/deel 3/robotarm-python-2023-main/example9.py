from RobotArm import RobotArm

robotArm = RobotArm('exercise 9')

# Jouw python instructies zet je vanaf hier:


for stapel in range(1,5):
	for blokje in range(stapel):
		robotArm.grab()
		for i in range(5):
			robotArm.moveRight()
		robotArm.drop()
		print(blokje, stapel)
		for i in range(4):
				robotArm.moveLeft()
		if not blokje == stapel - 1:
				robotArm.moveLeft()

# for stapel in range(1,11):
	# for blokje in range(1, stapel):
	# 	robotArm.grab()
	# 	for _ in range(5):
	# 		robotArm.moveRight()
	# 	robotArm.drop()
	# 	# for _ in range(5):
	# 	# 	robotArm.moveLeft()

	# robotArm.grab()
	# for i in range(5):
	# 	robotArm.moveRight()
	# robotArm.drop()
	# if stapel == 4:
	# 	for i in range(7):
	# 		robotArm.moveLeft()
	# elif  stapel == 7:
	# 	for i in range(6):
	# 		robotArm.moveLeft()
	# elif stapel == 9:
	# 	for i in range(5):
	# 		robotArm.moveLeft()
	# else:
	# 	if stapel <= 9:
	# 		for i in range(4):
	# 			robotArm.moveLeft()
	
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()