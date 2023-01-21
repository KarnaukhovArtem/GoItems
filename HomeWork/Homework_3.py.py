#1
given_string = '   i am gonna have my super power tomorrow morningso i am heading to bed now. Bye everyone   '
print( given_string.strip( ))
#1.2 -?
print(given_string.upper())
print(given_string.lower())
print(given_string.replace('super power', 'tasty breakfast'))
if given_string.isalpha():
    print('Good')
elif given_string.isalnum() :
    print('Your string with number')
print(given_string.replace(' ', '-'))
print(given_string.replace('i', '1'))
# чогось не працю набуть проблема функціях 2 3 4
print((given_string.strip( ), replace('super power', 'tasty breakfast'), replace('i', '1'), upper()))

#2
#3


while True:
    s = input("Знак (+,-,*,/): ")
    if s == '0':
        break
    if s in ('+', '-', '*', '/'):
        x = float(input("x= "))
        y = float(input("y= "))
        if s == '+':
            print(x+y)
        elif s == '-':
            print(x-y)
        elif s == '*':
            print(x*y)
        elif s == '/':
            if y != 0:
                print(x/y)
            else:
                print("Ділення на 0!")
    else:
        print("Неправельний знак!")

