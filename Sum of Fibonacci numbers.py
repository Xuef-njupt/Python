n = int(input('Enter number: '))
a = []

if (n == 1):
    print(1)
else:
    a.append(0)
    a.append(1)
    for i in range(n):
        a.append(a[i+1] + a[i])
        print(a[i+1])