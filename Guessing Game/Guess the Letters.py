#In this game you need to guess the word be letters. Game uses SOWPODS dictionary to generate words.
import random

a = ""

lines = open("sowpods.txt", "r")
for i in lines:
    a += i

a = a.split()
word = a[random.randint(1,276751)]
word_1 = word
print(word)
while(1):
    user_input = input("Guess the letter")
    user_input = user_input.upper()
    if(user_input == word[0]):
        word = word[:0] + word[(0 + 1):]
        if (len(word) <= 0):
            print("You win. Your word is: ", word_1)
            break
        print("You guess the letter :). Try next: ")
