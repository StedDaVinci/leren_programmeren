# name of student: 
# number of student:
# purpose of program: 
# structure of program: 

coinValues = [500, 200, 100, 50, 20, 10, 5, 2, 1]  

toPay = int(float(input('Amount to pay: ')) * 100)  
paid = int(float(input('Paid amount: ')) * 100)  
change = paid - toPay 

returned_coins = {}  

while change > 0 and len(coinValues) > 0: 

    coinValue = coinValues.pop(0)  
    nrCoins = change // coinValue  

    if nrCoins > 0:  
        print(f'return maximal {nrCoins} coins of {coinValue} cents!')  
        nrCoinsReturned = int(input(f'How many coins of {coinValue} cents did you return? '))  
        change -= nrCoinsReturned * coinValue  
        returned_coins[coinValue] = nrCoinsReturned  

if change > 0: 
    print(f'Change not returned: {change} cents')
else:
    print('done')  

print("Returned coins:")
for coinValue, count in returned_coins.items():
    print(f"{count} coins of {coinValue} cents returned")
