from RobotArm import RobotArm

robotArm = RobotArm()
robotArm.randomLevel(1,7)

# Jouw python instructies zet je vanaf hier:

for i in range(1,8):
	robotArm.grab()
	kleur = robotArm.scan()
	if kleur == "":
		break
	for _ in range(i): 
		robotArm.moveRight()
	robotArm.drop()
	for _ in range(i): 
		robotArm.moveLeft()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()
