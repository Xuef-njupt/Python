def Decryptor(string, step):
    result = ''

    for i in string:
        symbol = int(ord(i))
        result = result + chr(symbol - step)
    print(result)

def Encryptor(string, step):
    result = ''

    for i in string:
        symbol = int(ord(i))
        result = result + chr(symbol + step)
    print(result)


f = input('Decript (D) , Encript(E): ')
string = input('Enter string: ')

while True:
    try:
        step = int(input('Enter step: '))
    except ValueError:
        print('You enter inccorect value type . Try another one: ')
    else:break


if f == 'D':
    Decryptor(string, step)
if f == 'E':
    Encryptor(string, step)