import random

def game():

    print('Rock : 1 , Paper : 2 , Scissors : 3')

    bot_move = random.randint(1, 3)
    player_move = int(input('Your move: '))


    if (bot_move == 1):
        bot_choise = 'Rock'
    if (bot_move == 2):
        bot_choise = 'Paper'
    if (bot_move == 3):
        bot_choise = 'Scissors'

    if (player_move == 1 and bot_move == 3):
        print('You win . Bot choise : ',bot_choise)
    elif (player_move == 2 and bot_move == 1):
        print('You win . Bot choise : ',bot_choise)
    elif (player_move == 3 and bot_move == 2):
        print('You win . Bot choise : ',bot_choise)
    elif (player_move == bot_move):
        print('A draw')
    else:
        print('You lose. Bot choise : ', bot_choise)

game()