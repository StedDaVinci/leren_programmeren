from RobotArm import RobotArm

robotArm = RobotArm('exercise 4')

# Jouw python instructies zet je vanaf hier:
# 4 blokjes naar derde kolom
for i in range(4):
	robotArm.grab()
	for i in range(2):
		robotArm.moveRight()
	robotArm.drop()
	for i in range(2):
		robotArm.moveLeft()
# blauw blokje naar 2e kolom
robotArm.grab()
robotArm.moveRight()
robotArm.drop()

robotArm.moveRight()
for i in range(4):
	robotArm.grab()
	robotArm.moveLeft()
	robotArm.drop()
	robotArm.moveRight()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()