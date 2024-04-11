from RobotArm import RobotArm

robotArm = RobotArm('exercise 10')

# Jouw python instructies zet je vanaf hier:

for i in range(5):
	robotArm.grab()
	for _ in range(9 - (i * 2)):
		robotArm.moveRight()
	robotArm.drop()
	for _ in range(8 - (i * 2)):
		robotArm.moveLeft()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()