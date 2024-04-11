from RobotArm import RobotArm

robotArm = RobotArm('exercise 7')

# Jouw python instructies zet je vanaf hier:

robotArm.moveRight()
for x in range(5):
	for i in range(6):
		robotArm.grab()
		robotArm.moveLeft()
		robotArm.drop()
		if i <= 5:
			robotArm.moveRight()
	if x <= 4:
		for i in range(2):
			robotArm.moveRight()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()