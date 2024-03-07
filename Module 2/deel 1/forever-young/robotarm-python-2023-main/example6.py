from RobotArm import RobotArm

robotArm = RobotArm('exercise 6')

# Jouw python instructies zet je vanaf hier:

robotArm.moveRight()

for i in range(6):
	robotArm.grab()
	color = robotArm.scan()
	if color == 'red':
		robotArm.moveRight()
		robotArm.drop()
		robotArm.moveLeft()
	else:
		robotArm.moveLeft()
		robotArm.drop()
		robotArm.moveRight()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()