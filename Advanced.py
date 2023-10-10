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


f = open('abcd.txt','w')
list = ['Subham\n','Lohan\n','the\n','programmer\n','Hello\n','there!']
f.writelines(list)
print('Data is sucessfully written on the file.')
f.close()



f = open('abcd.txt','r')
list = f.readlines()
print(list)
for line in list:
    print(line,end='')
f.close()



with open('abcd.txt','r') as f:
    print(f.readlines())

print(f.closed)


with open('abcd.txt','r') as f:
    print(f.tell())
    print(f.read(4))
    print(f.tell())
    print(f.read(5))
    print(f.tell())



data = "All students are STUPIDS and DUMB"
f = open('abc.txt','w')
f.write(data)
with open('abc.txt','r+') as f:
    print(f.read())
    print('The current cursor position is :',f.tell())
    f.seek(17)
    print('The current cursor position is :',f.tell())
    f.write("GEMS and very obedient..!")
    f.seek(0)
    print('The current cursor position is ::',f.tell())
    print('Data after modification :: ',f.read())



import os,sys
print(os.path.isfile('abc.txt'))

fname = input('Enter filename :')
if os.path.isfile(fname):
    print("The file",fname, "exists")
    f = open(fname,'r')
    print(f.read())
    f.close()
else:
    print("The file",fname, "does not exists")
    sys.exit(0)


import os,sys
fname = input('Enter filename :')
if os.path.isfile(fname):
    print("The file",fname, "exists")
    f = open(fname,'r')
else:
    print("The file",fname, "does not exists")
    sys.exit(0)
lcount = wcount = ccount = 0
for line in f:
    lcount += 1
    ccount += len(line)
    words = line.split()
    wcount += len(words)
print("The number of lines :",lcount) 
print("The number of words :",wcount) 
print("The number of characters :",ccount) 
"""

# Handling Binary Data in python

"""
f1 = open("Guido.jpg",'rb')
f2 = open("Guido_new_pic.jpg",'wb')
bytes = f1.read()
f2.write(bytes)
print("New image is available with the name: Guido_new_pic.jpg")


import csv
with open("emp.csv",'w',newline='') as f:
    w = csv.writer(f) 
    w.writerow(['ENO','ENAME','ESAL','EADDR'])
    n=int(input('Enter number of emplyoees:'))
    for i in range(n):
        eno = int(input("Enter employee number:"))
        ename = input('Enter employee name:')
        esal = float(input("Enter employee salary:"))
        eaddr = input("Enter address of employee:")
        w.writerow([eno,ename,esal,eaddr])
print("Total employees data written to csv file sucessfully.")



import csv
f = open('emp.csv','r')
r = csv.reader(f)
data = list(r)
for line in data:
    for word in line:
        print(word,"\t",end='')
    print()


import pickle

class employee:
    def __init__(self,eno,ename,esal,eaddr):
        self.eno = eno
        self.ename = ename
        self.esal = esal
        self.eaddr = eaddr
    def display(self):
        print(self.eno,'\t',self.ename,'\t',self.esal,'\t',self.eaddr)

with open('emp.dat','wb') as f:
    e = employee(100,'Durga',10000,'Hyderabad')
    pickle.dump(e,f)
    print('Pickling is done.')

with open('emp.dat','rb') as f:
    obj = pickle.load(f)
    print('Employee information after pickling...')
    obj.display()
    print(obj)



####### Object Oriented Programming(OOPs) ########


class student:
    def read(self):
        print('Reading the python...!')

s = student()
s.read()


class student:
    def __init__(self,name,rollno,marks):
        self.name = name
        self.rollno = rollno
        self.marks = marks

s1 = student("Subham",456,87)
print(s1.name,s1.rollno,s1.marks)

s2 = student('sunny',102,98)
print(s2.name,s2.rollno,s2.marks)


class student:
    def __init__(self,name,rollno,marks):
        self.name = name
        self.rollno = rollno
        self.marks = marks
    def disply(self):
        print("student name : {} , Roll number : {} and Marks : {}".format(self.name,self.rollno,self.marks))

s1 = student("Subham",456,87)
s2 = student('sunny',102,98)
s1.disply()
s2.disply()


a = 10                                 # this is a global variable
class student:
    cname = 'DURGESOFT'                # this is a static variable
    def student(self,name,rollno):
        self.name = name               # this is an instance variable
        self.rollno = rollno
    def m1(self):
        x = 50                         # this is a local variable

s1 = student()
s2 = student()
print(s1.cname)
print(s2.cname)
s1.m1()
print(student.cname)



class Student:
    def __init__(self):
        self.name = 'Subham'
        self.rollno = 102
        self.marks = 96
    def talk(self):            # self is a keyword which is available inside the class.
        print("Hello ! My name is : ",self.name)
        print("My rollno is : ",self.rollno)
        print("My Marks  is : ",self.marks)


s1 = Student()
print(s1.name,'\t',s1.marks,'\t',s1.rollno)
s1.talk()



class Test:
    def __init__(self):
        self.a = 1000
        self.b = 2000
    def m1(self):
        self.c = 3000
        self.d = 4000
t1 = Test()
t1.m1()
print(t1.__dict__)      #this is to get the instance variable values in the form of key-value pair.
print(t1.a,t1.b,t1.c,t1.d)

t2 = Test()
t2.a = 8888
t2.b = 9999
print(t2.__dict__)

t3 = Test()
t3.m1()
t3.e = 5678
t3.f = 1234
t3.g = 7890            # we can assign as many instance variable as we want outside class using reference variable 
print(t3.__dict__)



class School:
    def __init__(self):
        self.a = 12
        self.b = 24
        self.c = 48
        self.d = 96

t1 = School()
t2 = School()
del t1.c                 # to delete a instance variable.
t2.e = 189               # adding extra instance variable.

print("t1 : ",t1.__dict__)
print("t2 : ",t2.__dict__)



class test:
    a = 10
    def __init__(self):
        self.b = 20

t1 = test()
t2 = test()
print(test.a)             #accesing static variable using class name(recommended)
print("t1 : ",t1.a,t1.b)
print("t2 : ",t2.a,t2.b)
test.a = 1000
t1.b = 2000
print("t1 : ",t1.a,t1.b)
print("t2 : ",t2.a,t2.b)



class Test:
    a = 10
    def __init__(self):
        self.b = 20
        Test.c = 30
    def m1(self):
        self.d = 40
        Test.e = 50
    
    @classmethod
    def m2(cls):
        cls.f = 60
        Test.g = 70
    
    @staticmethod
    def m3():
        Test.h = 80

t1 = Test()
t1.m1()
Test.m2()
Test.m3()
Test.i = 90
print(Test.__dict__)


class Test:
    a = 10
    def __init__(self):
        print(self.a)
        print(Test.a)
    def m1(self):
        print(self.a)
        print(Test.a)
    
    @classmethod
    def m2(cls):
        print(cls.a)
        print(Test.a)
    
    @staticmethod
    def m3():
        print(Test.a)

t1 = Test()
t1.m1()
t1.m2()
t1.m3()


class TEST:
    a = 10
    def __init__(self):
        self.b = 20

t1 = TEST()
t2 = TEST()
t2.a += 1
print(t2.a)
print(TEST.a)
print(t1.a)



class test:
    a = 10
    def m1(self):
        self.a = 20

t1 = test()
t1.m1()
print(test.a)
print(t1.a)



class test:
    x = 10
    def __init__(self):
        self.y = 20

t1 = test()
t2 = test()
t1.x += 1
t2.y += 1
print('t1 : ',t1.x,t1.y)  # 11 20
print('t2 : ',t2.x,t2.y)  # 10 21
print('test : ',test.x)   # 10


class Sample:
    a = 10
    def __init(self):
        self.b = 20
t1 = Sample()
t2 = Sample()
Sample.a = 1000
t1.b = 40
print('t1:',t1.a,t1.b)
print('t2:',t2.a,t2.b)


class Sample:
    a = 10
    def __init__(self):
        self.b=20
    def m1(self):
        self.a = 1000
        self.b = 2000
t1 = Sample()
t2 = Sample()
t1.m1()
print('t1 :',t1.a,t1.b)
print('t2 :',t2.a,t2.b)


class Sample:
    a = 10
    def __init__(self):
        self.b=20
    @classmethod
    def m1(cls):
        cls.a = 888
        cls.b = 999
t1 = Sample()
t2 = Sample()
t1.m1()
print('t1 :',t1.a,t1.b)
print('t2 :',t2.a,t2.b)
print('Sample :',Sample.a,Sample.b)


class Delete:

    a = 10
    @classmethod
    def m1(cls):
        del cls.a

Delete.m1()
print(Delete.__dict__)



import sys
class Customer:
    bankname = "Lohan's Bank"
    def __init__(self,name,balance= 0.0):
        self.name = name
        self.balance = balance
    def deposit(self,amt):
        self.balance += amt
        print('Balance after deposit:',self.balance)
    def withdraw(self,amt):
        if amt>self.balance:
            print('Insufficient Funds: cannot perform the operation.')
            sys.exit()
        self.balance = self.balance - amt
        print('Balance after withdwar :',self.balance)

print('Welcome to ',Customer.bankname)
name = input('Enter your name please!')
c = Customer(name)
while True:
    print('d-Deposit\nw-Withdraw\ne-Exit')
    option=input('Choose what you want : ')
    if option == 'd' or option=='D':
        amt = float(input('Enter amount: '))
        c.deposit(amt)
    elif option=='w' or option=='W':
        amt = float(input('Enter amount: '))
        c.withdraw(amt)
    elif option=='e' or option=='E':
        print('Thanks for Banking with Lohan !!')
        sys.exit()
    else:
        print('Invalid option entered ')



class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def display(self):
        print('Hi ',self.name)
        print('your marks are:',self.marks)
    def grade(self):
        if self.marks >=60:
            print('Hurray! you got First grade.')
        elif self.marks >=50:
            print('you got second grade.')
        elif self.marks >=40:
            print('you got third grade.')
        else :
            print('GO HOME...you got failed.')

n = int(input('Enter number of students : '))
for i in range(n):
    name = input('Enter student name : ')
    marks = int(input('Enter student marks : '))
    s = Student(name,marks)
    s.display()
    s.grade()



class Student:
    def setName(self,name):
        self.name = name
    def getName(self):
        return self.name
    def setMarks(self,marks):
        self.marks = marks
    def getMarks(self):
        return self.marks
    
n = int(input('Enter number of students : '))
for i in range(n):
    name = input('Enter name of the student: ')  
    marks = int(input('Enter marks of the student: '))
    s = Student()
    s.setName(name)
    s.setMarks(marks)
    print('Hi ',s.getName())
    print('Your marks are :',s.getMarks())
    print()



class Animal:
    legs = 4
    @classmethod
    def walk(cls,name):
        print('{} walks with {} legs'.format(name,cls.legs))

Animal.walk('Dog')
Animal.walk('Cat')


'''WAP to track the number of objects for a class?'''
class test:
    count = 0
    def __init__(self):
        test.count += 1
    @classmethod
    def noofobjects(cls):
        print('The number of objects are :',cls.count)
t1 = test()
t2 = test()
test.noofobjects()



class Test:
    def add(x,y):
        print('The sum is :',(x+y))
    def product(x,y):
        print('The product is :',x*y)
    def average(x,y):
        print('The average is :',(x+y)/2)
Test.add(10,20)
Test.product(10,20)
Test.average(10,20)


class Test:
    count =0
    def __init__(self):
        Test.count += 1
    @staticmethod            # there is no compulstion to declare the decorator for the static method.
    def countit():
        print('The number of objects are :',Test.count)

t1 = Test()
t2 = Test()
t3 = Test()
t4 = Test()
t5 = Test()
Test.countit()


class Employee:
    def __init__(self,eno,ename,esal):
        self.eno = eno
        self.ename = ename
        self.esal = esal
    def display(self):
        print('Employee Number :',self.eno)
        print('Employee name :',self.ename)
        print('Employee Salary :',self.esal)
class test:
    def modify(emp):
        emp.esal += 5000
        emp.display()
e = Employee(101,'Subham',15000)
test.modify(e)



class Outer:
    def m1(self):
        print('Outer class Method!')
    class Inner:
        def m2(self):
            print('Inner class method!')

x = Outer()
y = x.Inner()             # outer class object must be referrenced to call inner class object.
x.m1()
y.m2()
Outer().Inner().m2()     # another way.
i = Outer().Inner()
i.m2()                   # another way.


class Person:
    def __init__(self):
        self.name = 'Subham'
        self.db = self.Dob()
    def display(self):
        print('The name of the person : ',self.name)
    class Dob:
        def __init__(self):
            self.dd = 26
            self.mm = 9
            self.yy = 1996
        def display(self):
            print('DOB is {}/{}/{}'.format(self.dd,self.mm,self.yy))

p = Person()
d = p.Dob()
p.display()
d.display()


class Human:
    def __init__(self):
        self.name = 'Sunny Deol'
        self.head = self.Head()
        self.brain = self.Brain()
    def display(self):
        print('Hello ! ',self.name)
    class Head:
        def talk(self):
            print('talking.....!')
    class Brain:
        def think(self):
            print('thinking...!!')

h = Human()
h.display()
h.head.talk()
h.brain.think()
"""


# Garbage Collector




