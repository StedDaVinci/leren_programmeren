antwoord1 = input("Is de kaas geel? (ja/nee): ").lower()

if antwoord1 == "ja":
    antwoord2 = input("Zitten er gaten in de kaas? (ja/nee): ").lower()
    
    if antwoord2 == "ja":
        antwoord3 = input("Is de kaas belachelijk duur? (ja/nee): ").lower()
        
        if antwoord3 == "ja":
            print("De kaas die je in gedachten hebt, is Emmentaler.")
        else:
            print("De kaas die je in gedachten hebt, is Leerdammer.")
    
    else:
        antwoord4 = input("Is de kaas hard als steen? (ja/nee): ").lower()
        
        if antwoord4 == "ja":
            print("De kaas die je in gedachten hebt, is Parmigiano Reggiano.")
        else:
            print("De kaas die je in gedachten hebt, is Goudse kaas.")
            
else:
    antwoord5 = input("Heeft de kaas blauwe schimmels? (ja/nee): ").lower()
    
    if antwoord5 == "ja":
        antwoord6 = input("Heeft de kaas een korst? (ja/nee): ").lower()
        
        if antwoord6 == "ja":
            print("De kaas die je in gedachten hebt, is Roquefort.")
        else:
            print("De kaas die je in gedachten hebt, is Camembert.")
    
    else:
        antwoord7 = input("Heeft de kaas een korst? (ja/nee): ").lower()
        
        if antwoord7 == "ja":
            print("De kaas die je in gedachten hebt, is Camembert.")
        else:
            print("De kaas die je in gedachten hebt, is Mozzarella.")