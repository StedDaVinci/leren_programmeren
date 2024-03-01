gastheer = True
gasten = False
drank = False
chips = True

if (gastheer and drank) or (gasten and chips and drank):
    print('Start the Party')
else:
    print('No Party')

