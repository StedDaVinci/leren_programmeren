gastheer = input("Wie is de gastheer? ").lower()
gasten = int(input("hoeveel gasten zijn er?"))
drank = False
chips = False

genoeg_gasten = gasten >= 4 and gasten <= 20
party_stef = gastheer == "stef" and genoeg_gasten
party_gasten = genoeg_gasten and drank and chips and not gastheer == "eugene"
party_gastheer = drank and len(gastheer) > 0 and not gastheer == "eugene" and genoeg_gasten





if party_stef or party_gasten or party_gastheer:
    print('Start the Party')
else:
    print('No Party')

