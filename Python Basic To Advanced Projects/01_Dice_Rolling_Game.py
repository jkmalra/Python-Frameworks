import random


while True:
    choice = input("Welcome to Dice Rolling Simulator! Roll the Dice(y/n): ").lower()
    if choice == 'y':
        dice1 = random.randint(1,9)
        dice2 = random.randint(1,9)
        print(f'{dice1},{dice2}')
    elif choice == 'n':
        print('Thankuou for playing')
        break
    else:
        print('--Invalid Input--')
    


# Dice Rolling Game

# - A simple Python program that simulates rolling two dice.
# - Uses random.randint() to generate numbers.
# - Takes user input to roll again or exit.
# - Demonstrates while loops, conditionals, and input handling.


#Loop
    #Ask: roll the dice(y/n)?
    #if yes:
    #   generate two random number between 1-6
    #   print them
    #if no:
    #   print thankyou for playing
    #   Quit()
    #else
    #   Print invalid choice