import random

#selecteer 2 nummers
num1 = random.randint(1,10)
num2 = random.randint(5,15)

#vraag om een antwoord
number = int(input(f'Weet jij wat {num1} + {num2} is? '))

#geef reactie op het antwoord
try:
    if number == num1 + num2:
        print('Dat is juist')
    elif number != num1 + num2:
        print('Nee dat klopt niet')
except ValueError:
    print('Dat is geen nummer!')
