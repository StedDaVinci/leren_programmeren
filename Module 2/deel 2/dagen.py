dagen = ("maandag", "dinsdag", "woensdag", "donderdag", "vrijdag", "zaterdag", "zondag")

print("alle dagen in de week zijn:", ', '.join(dagen))
print("de werkdagen zijn:", ', '.join(dagen[0:5]))
print("de weekenddagen zijn:", ', '.join(dagen[5:7]))
print("alle dagen van de week in omgekeerde volgorde zijn:", ', '.join(reversed(dagen)))
print("De werkdagen in omgekeerde volgorde zijn:", ', '.join(reversed(dagen[0:5])))
print("De weekenddagen in omgekeerde volgorde zijn:", ', '.join(reversed(dagen[5:7])))