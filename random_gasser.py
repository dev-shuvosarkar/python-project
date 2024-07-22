# some chatGPT currection included 

import random

while True:
    top_of_range = input('Enter the top range to guess: ')

    if top_of_range.isdigit():
        top_of_range = int(top_of_range)
        if top_of_range > 0:
            break
        else:
            print('Please type a number larger than 0 next time.')
    else:
        print('Please enter a valid number.')
    
random_number = random.randint(1, top_of_range)
total_guess = 0

while True:
    total_guess += 1
    user_guess = input('Guess a number: ')

    if user_guess.isdigit():
        user_guess = int(user_guess)

        if random_number == user_guess:
            print('You got it!')
            break
        elif user_guess > random_number:
            print('You are above the number.')
        else:
            print('You are below the number.')
    else:
        print('Please enter a valid number.')

print(f'You got it in {total_guess} guesses.')
