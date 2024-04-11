from RobotArm import RobotArm

robotArm = RobotArm('exercise 11')

# Jouw python instructies zet je vanaf hier:

for i in range(8):
	robotArm.moveRight()
for blokje in range(1,10):
	robotArm.grab()
	kleur = robotArm.scan()
	if kleur == "white":
		robotArm.moveRight()
		robotArm.drop()
		if blokje <= 8:
			for _ in range(2):
				robotArm.moveLeft()
	else:
		robotArm.drop()
		robotArm.moveLeft()
	
# 	if i >= 2 and i <= 7:
# 		robotArm.moveRight()
# 	robotArm.grab()
# 	kleur = robotArm.scan()
# 	if kleur == "white":
# 		robotArm.drop()
# 		robotArm.moveRight()
# 		robotArm.grab()
# 		kleur2 = robotArm.scan()
# 		if kleur2 == "white":
# 			robotArm.moveRight()
# 			robotArm.drop()
# 			for _ in range(2): 
# 				robotArm.moveLeft()
# 			robotArm.grab()
# 			robotArm.moveRight()
# 			robotArm.drop()
# 			robotArm.moveRight()
# 		else:
# 			robotArm.drop()
# 			robotArm.moveLeft()
# 			robotArm.grab()
# 			robotArm.moveRight()
# 			robotArm.drop()
# 	else:
# 		robotArm.drop()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()