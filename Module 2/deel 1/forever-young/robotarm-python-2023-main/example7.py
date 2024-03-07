from RobotArm import RobotArm

robotArm = RobotArm('exercise 7')
for i in range(5):
	robotArm.moveRight()
	for i in range(6):
		robotArm.grab()
		robotArm.moveLeft()
		robotArm.drop()
		robotArm.moveRight()
	robotArm.moveRight()
robotArm.wait()