#You need to guess the randomly gengerate number from 1 up to 10. Programm give a hint about you need smaller or larger number.
import random

number = random.randint(1,10)

attempts = 0

def game():

    while True:

            try:
                guess = int(input('Enter number: '))
            except ValueError:
                print('You don`t enter number , try one more time : ')
            if (guess > 0 and guess < 11):
                global attempts
                attempts = attempts + 1

                if (guess == number):
                    print('You guess the correct number . You win .')
                    print('You use : ', attempts , ' attempts')
                    break
                elif (guess > number):
                    print('Try smaller number: ')
                elif (guess < number):
                    print('Try larger number: ')

game()
