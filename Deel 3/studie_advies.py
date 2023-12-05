from studieadviestext import *

vraag1 = int(input(COMPETENTIE_STELLING_1 + OPTIES))

vraag2 = int(input(COMPETENTIE_STELLING_6 + OPTIES))

gemiddelde_score = (vraag1 + vraag2) / 2

if gemiddelde_score <= 2:
	print(COMPETENTIE_ADVIES_ZORGELIJK)

elif gemiddelde_score <= 3:
	print(COMPETENTIE_ADVIES_TWIJFELACHTIG)

elif gemiddelde_score >= 4:
	print(COMPETENTIE_ADVIES_GERUSTSTELLEND)