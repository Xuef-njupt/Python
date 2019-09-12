#You need to guess 4 digit number.
#For every correct number in correct order programm print 1 bull.
#For every correct number but in wrong order programm need to print 1 cow ,
#but this function now is under development(when generated number contain more than one exact number programm write that
#there is 4 cows or even more).
import random

def game(number):
    while(True):
        user_num = int(input("Enter number: "))

        bulls = 0
        cows = 0

        if(user_num == number):
            print("You win.")
            break

        user_num_1 = []
        number_1 = []

        for i in range(4):
            user_num_1.append(int(str(user_num)[i]))

        for i in range(4):
            number_1.append(int(str(number)[i]))

        for i in range(4):
            if (user_num_1[i] == number_1[i]):
                bulls += 1
            for j in range(4):
                if(user_num_1[i] == number_1[j] and user_num_1[i] != number_1[i]):
                    cows += 1
                    for k in range(10):
                        count_user_num = user_num_1.count(k)
                        count_num = number_1.count(k)
                        if ( count_user_num > 0 and  count_num > count_user_num and count_num > count_user_num):
                            cows -= count_user_num - count_num

        print("Bulls is: ", bulls)
        print("Cows is: ", cows)

number = random.randint(1000,9999)

print(number)

game(number)