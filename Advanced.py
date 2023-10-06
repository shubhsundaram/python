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



try:
    print('Try!')
finally:
    print('finally without exception!')

try:
    print('Try!')
    print(10/0)
finally:
    print('finally')


try:
    print('try')
except:
    print('except')
else:
    print('else')


try:
    print('try')
except:
    print('except')
else:
    print('else1')
else:
print('else2')


try:
    print('try')
except:
    print('except')
finally:
    print('finally')
finally:
print('finally')


try:
    print('try')
print('Hello')
except:
    print('except')



try:
    print('Try')
except:
    print('Except')
if 10>40:
    print('if')
else:
    print('else')  # here else is related to if statement



try:
    print('Try')
except:
    print('Except')
finally:
    try:
        print('inner try')
    except:
        print('Inner except')
    finally:
        print('Inner finally')


Conclusion:
1.) whenever we are using 'try' block it is compulsory to use either 'except' or 'finally' block.
2.) only 'except' block is invalid
3.) 'finally' without try is invalid.
4.) 'else' without except is also invalid.
5.) 'try-except-else-finally' this order is mandatory.
6.) we can take complete 'try-except-else-finally' inside 'try','except','else' and 'finally' blocks.





class TooYoungException(Exception):
    def __init__(self,arg):
        self.msg = arg

class TooOldException(Exception):
    def __init__(self,arg):
        self.msg = arg

age = int(input("Enter the age:"))
if age>60:
    raise TooYoungException("please wait some more time you will get a good match soon...!!")
elif age<18:
    raise TooOldException("Your age crossed marriage age , no chance for you to get married...!!")
else:
    print("Thanks for registration...your will get details by mail soon..!")
"""



# PYTHON LOGGING

"""
import logging

logging.basicConfig(filename='log.txt',level=logging.DEBUG)

logging.info("A new request came.")
try:
    x = int(input("enter first number :"))
    y = int(input("enter second number :"))
    print('x/y = ',x/y)
except ZeroDivisionError as msg:
    print('Cannot divide with 0')
    logging.exception(msg)
except ValueError as msg:
    print('Please enter int value only')
    logging.exception(msg)
logging.info('request processing completed!!')
"""

# ASSERTIONS AND DEBUGGING

"""
def square(x):
    return x*x

assert square(2)==4,'the square of 2 should be 4'
assert square(3)==9,'the square of 3 should be 9'
assert square(4)==16,'the square of 4 should be 16'

print(square(2))
print(square(3))
print(square(4))
"""

# FILE HANDLING

"""
f = open('abc.txt','w')
print("file Name : ",f.name)
print("file Mode : ",f.mode)
print("Is file readable or not? : ",f.readable())
print("Is file writable or not? : ",f.writable())
f.close()
print("Is file closed or not? : ",f.closed)


f = open('abc.txt','r')
print("file Name : ",f.name)
print("file Mode : ",f.mode)
print("Is file readable or not? : ",f.readable())
print("Is file writable or not? : ",f.writable())
f.close()
print("Is file closed or not? : ",f.closed)


f = open('abcd.txt','x')    # exclusive creation mode only work for the files which are not already created
print("file Name : ",f.name)
print("file Mode : ",f.mode)
print("Is file readable or not? : ",f.readable())
print("Is file writable or not? : ",f.writable())
f.close()
print("Is file closed or not? : ",f.closed)


f = open('abcd.txt','w')
f.write('durga\n')
f.write('software\n')
f.write('solutions\n')
print('Data is sucessfully written on the file.')


f = open('abcd.txt','a')
f.write('durga\n')
f.write('software\n')
f.write('solutions\n')
print('Data is sucessfully written on the file.')
"""

f = open('abcd.txt','w')
list = ['Subham\n','Lohan\n','the\n','programmer']
f.writelines(list)
print('Data is sucessfully written on the file.')
f.close()



