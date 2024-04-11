import random

def main():
    secret_number = random.randint(1, 1000)
    rounds = 0
    score = 0

    while rounds < 20:
        guess = input("Raad een getal tussen 1 en 1000 (of typ 'stop' om te stoppen): ")
        
        if guess.lower() == 'stop':
            break
        
        try:
            guess = int(guess)
        except ValueError:
            print("Ongeldige invoer. Probeer opnieuw.")
            continue

        rounds += 1

        if guess == secret_number:
            print("Gefeliciteerd! Je hebt het juiste getal geraden!")
            score += 1
            break
        elif rounds >= 10:
            print("Helaas, je hebt al 10 keer geraden. De ronde eindigt.")
            break
        else:
            difference = abs(secret_number - guess)
            if difference < 20:
                print("Je bent heel warm")
            elif difference < 50:
                print("Je bent warm")
            else:
                print("Je bent koud")
        
        score += 1

    print(f"Eindscore: {score}")

if __name__ == "__main__":
    main()
