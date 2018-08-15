from cs50 import get_float

while True:
    change = get_float("O hai! How much change is owed: ")
    if change > 0:
        break

change *= 100
change = round(change)
coins = 0

while change >= 25:
    change -= 25
    coins += 1

while change >= 10:
    change -= 10
    coins += 1

while change >= 5:
    change -= 5
    coins += 1

while change >= 1:
    change -= 1
    coins += 1

print(coins)

# Will come back and implement using %