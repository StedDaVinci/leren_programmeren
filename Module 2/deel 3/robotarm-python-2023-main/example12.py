from RobotArm import RobotArm

robotArm = RobotArm('exercise 12')

# Jouw python instructies zet je vanaf hier:

for _ in range(8):
	robotArm.moveRight()
for x in range(1,10):
	robotArm.grab()
	kleur = robotArm.scan()
	if kleur == "red":
		for _ in range(x): 
			robotArm.moveRight()
		robotArm.drop()
		for _ in range(x): 
			robotArm.moveLeft()
	else: 
		robotArm.drop()
	if x <= 8:
		robotArm.moveLeft()


# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()