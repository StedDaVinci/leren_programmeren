GROEPGROOTTE = 4
TICKETS = 745
VRPER5MIN = 37 
LENGTEVR = 45
PER5MIN = 5

hoelangvr = LENGTEVR / PER5MIN
kostentickets = GROEPGROOTTE * TICKETS
perpersoonvr = VRPER5MIN * hoelangvr
totaalvrkosten = perpersoonvr * GROEPGROOTTE
allestotaal = totaalvrkosten + kostentickets

print(f"Dit geweldige dagje-uit met {GROEPGROOTTE} mensen in de Speelhal met {LENGTEVR} minuten VR kost je maar {allestotaal} cent")
