# EXCEPTION HANDLING

print('statement-1')
try:
    print(10/0)
except ZeroDivisionError:
    print(10/2)
print('Statement-3')


try:
    x = int(input("Enter a number:"))
    y = int(input("Enter another number:"))
    print('x/y = ', x/y)
except (ZeroDivisionError,ValueError) as msg:
    print('Please enter valid input since :',msg)


#hello python

