gastheer = input("Wie is de gastheer? ").lower()
gasten = False
drank = False
chips = False


party_stef = gastheer == "stef"
party_gasten = gasten and drank and chips and not gastheer == "eugene"
party_gastheer = drank and len(gastheer) > 0 and not gastheer == "eugene"






if party_stef or party_gasten or party_gastheer:
    print('Start the Party')
else:
    print('No Party')

