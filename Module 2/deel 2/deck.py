import random

kleuren = ["harten", "klaveren", "schoppen", "ruiten"]
pestkaarten = ["aas", "vrouw", "heer", "boer"]
deck = []
je_hand = []

for kleur in kleuren:
	for i in range(2, 11):
		deck.append(f"{kleur} {i}")
	for pestkaart in pestkaarten:
		deck.append(f"{kleur} {pestkaart}")

deck.extend(["joker"] * 2)

random.shuffle(deck)

je_hand = deck[:7]
print(je_hand)
del deck[:7]
# for i in range(7):
# 	je_hand.append(deck.pop(0))
# print(je_hand)


for kaart in je_hand:
	print(f"kaart {len(je_hand)}: {kaart}")
print()
print(f"deck ({len(deck)} kaarten):", deck)
