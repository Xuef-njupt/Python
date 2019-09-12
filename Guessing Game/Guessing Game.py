print("In this game computer need to guess your number")
print("If your number is bigger - print 1 ; if smaller - print 2 ; if equal - print 3")
a = [14,13,12,11,10,9,8,7,6,5,4]
i = 0
num = a[i]
count = 0
print(num)
while(1):

    hint = int(input("Enter next order: "))
    if (hint == 3):
        print("Game over. Computer needs: ", count ," moves")
        break
    if(hint == 2):
        num -= 1
        print(num)
    if(hint == 1):
        i += 1
        num = num + a[i]
        print(num)
    count += 1