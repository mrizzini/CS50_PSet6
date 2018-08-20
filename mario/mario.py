from cs50 import get_int

brick = 2

while True:
    n = get_int("Height: ")
    if n >= 0 and n <= 23:
        count = n - 1
        break

# Prints this many rows
for i in range(n):
    # // Prints out the correct amount of spaces for the first row of bricks, using the count variable
    for num in range(0, count):
        print(" ", end="")
    # Prints out this many columns
    for j in range(0, brick):
        print("#", end="")
    # Prints a line break after the row is complete
    print()
    brick += 1
    count -= 1
