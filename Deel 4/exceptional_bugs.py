import random

#selecteer 2 nummers
num1 = random.randint(1,10)
num2 = random.randint(5,15)

#vraag om een antwoord
try:
    number = int(input(f'Weet jij wat {num1} + {num2} is? '))


    
except ValueError:
    print('Dat is geen nummer!')
else:
    if number == num1 + num2:
        print('Dat is juist')
    else:
        print('Nee dat klopt niet')
#geef reactie op het antwoord



