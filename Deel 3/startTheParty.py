gastheer = True
gasten = True
drank = True
chips = True

if (gastheer and (gasten or chips or drank)) or (gasten and (chips or drank)) or (chips and drank):
    print('Start the Party')
else:
    print('No Party')

