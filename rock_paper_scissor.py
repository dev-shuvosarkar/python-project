import random

print('*****************************************')
print('   Welcome to Rock Paper Scissor Game!   ')
print('*****************************************')
win = 0
loose = 0
ties = 0


while True:
    user_move = input('Choose Your move (rock, paper, or scissor) or type "Q" to exit: ').lower()
    
    if user_move == 'q':
        break

    random_number = random.randint(1, 3)
    computer_move = ''


    if random_number == 1:
        computer_move = 'rock'
    elif random_number == 2:
        computer_move = 'paper'
    elif random_number == 3:
        computer_move = 'scissor'


    if user_move == computer_move:
        print('Tie')
        ties += 1
    elif (user_move == 'rock' and computer_move == 'scissor') or \
        (user_move == 'paper' and computer_move == 'rock') or \
        (user_move == 'scissor' and computer_move == 'paper'):
        print('You win!')
        win += 1
    elif (user_move == 'rock' and computer_move == 'paper') or \
        (user_move == 'paper' and computer_move == 'scissor') or \
        (user_move == 'scissor' and computer_move == 'rock'):
        print('You lose!')
        loose += 1
    else:
        print('Invalid input')
        print('please choose (rock, paper or scissor)')
        continue

    print('-----------------------------------------------------------')
    print(f'You chose **{user_move}** and coputer chose **{computer_move}**')
    print(f'wins: {win}, looses: {loose}, ties: {ties}')
    print('-----------------------------------------------------------')


print('**************************************************************')
print(f'Your fonal score is -> {win} wins, {loose} looses and {ties} ties')
print('Thanks for playing. Good buy!')
print('**************************************************************')