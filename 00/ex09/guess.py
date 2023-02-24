import random
import sys

x = random.randint(1, 99)
n = 0
tries = 0
print("This is an interactive guessing game!")
print("You have to enter a number between 1 and 99 to find out the secret number.")
print("Type 'exit' to end the game.\n")
while n != x:
    tries += 1
    n = input("What's your guess between 1 and 99?\n>>")
    if n == "exit":
        sys.exit()
    n = int(n)
    if n < x:
        print("Too low!")
    if n > x:
        print("Too high!")
if tries == 1:
    print("You're a genius!! you've got it in the first try!!")
else:
    if n == 42:
        print("The answer to the ultimate question of life, the universe and everything is 42.")
    print("Congratulations, you've got it!")
    print("You won in " + str(tries) + " attempts!")
