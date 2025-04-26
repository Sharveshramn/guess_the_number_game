import random
import math

print("Welcome to the number guessing game.")
print("Press 1 to start")
print("Press 0 to wait")

Start_Input = int(input())

if Start_Input == 1:
    print("enter the maximum number to guess")
    upper = int(input())
    print("enter the minimum number to guess is ")
    lower = int(input())
    The_number_to_guess = random.randint(lower,upper)  # includes upper limit and lower limit
    Number_of_chances = math.ceil(math.log2(upper - lower + 1)) #used to guess the avg no of chances needed to guess
    print(f'Number of chances is {Number_of_chances}')
    
    guess_counter = 0
    while guess_counter < Number_of_chances:
        guess_counter = guess_counter + 1
        my_guess = int(input(f"Enter your {guess_counter} guess: "))
        if guess_counter == Number_of_chances - 1:
            print("⚠️ This is your last chance!")
        if my_guess == The_number_to_guess:
            win = True
            print(f"Wowwww u won in {guess_counter}th guess🥳🥳🥳")
            break
        elif my_guess < The_number_to_guess:
            print("You guessed low, guess somewhat higher number")
        elif my_guess > The_number_to_guess:
            print("You guessed high, guess somewhat lower number")
        else:
            print("enter a valid number")
    
    if Number_of_chances == guess_counter and win == False:
        print("Opps you lost😔.... Bettter luck next time")
        print(f"The correct number is {The_number_to_guess}")
elif Start_Input == 0:
    print('Let me know when you are ready, see you soon!')
else:
    print("Invalid input.")
