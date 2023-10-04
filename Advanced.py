# EXCEPTION HANDLING

"""
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


try:
    x = int(input("Enter first number:"))
    y = int(input("Enter second number:"))
    print("x/y = ",x/y)
except ZeroDivisionError:
    print("cannot divide with zero!")
except:
    print("Default Except:Please provide valid input")
"""


try:
    print('Outer try block.')
    try:
        print("Inner try block")
        print(10/0)
    except ZeroDivisionError:
        print("Inner except block")
    finally :
        print("Inner finally block")
except:
    print('Outer except block')
finally:
    print('Outer finally block')



try:
    print('Try')
    print(10/0)
except:
    print('Except')
else:
    print('else')
finally:
    print('finally')



