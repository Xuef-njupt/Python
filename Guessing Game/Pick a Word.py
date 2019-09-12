import random

a = ""

lines = open("sowpods.txt", "r")
for i in lines:
    a += i

a = a.split()
print(a[random.randint(1,276751)])