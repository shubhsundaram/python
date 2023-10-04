'''a,b,c = [float(x) for x in input('Enter three numbers:').split(',')]
print('the sum of these numebrs is :',(a+b+c))
print('the product of these numebrs is :',(a*b*c))


# Evaluate function
a,b,c = [eval(x) for x in input('Enter three inputs here:').split()]
print(type(a))
print(type(b))
print(type(c))

import sys
from sys import argv
args = argv[1:]
sum=0
for x in args:
    n = int(x)
    sum +=n
print('The sum:',sum)
'''

# Conditional Statement (if,if-else and if-elif-else)
'''name = input("enter name:")
if name == 'Durga':
    print("hello %s ! How are you" %name)
else:
    print('Hello %s have a nice day' %name)

    
brand = input('Enter your favourite brand:')
if brand == 'RC':
    print('It is for newbies')
elif brand == 'KF':
    print('Cheers')
elif brand == 'Gin':
    print("holla! chhers buddy")
else:
    print('Please drink good brands')

    

num1,num2,num3 = [eval(x) for x in input("enter three numbers: ").split()]
if(num1>num2 and num1>num3):
    print('The biggest number is: ' ,num1)
elif(num2>num3):
    print('The biggest number is: ' ,num2)
else:
    print("The biggest number is: " ,num3)

    
num = eval(input("enter a number:"))
if (num>=1 and num<=100):
    print('the number',num, 'is between  1 and 100')
else:
    print('the number',num, 'is not between  1 and 100' )

    
digit = int(input('enter a digit betwenn 1 and 10:'))
if(digit == 1):
    print('ONE')
elif(digit==2):
    print('TWO')
elif(digit==3):
    print('THREE')
elif(digit==4):
    print('FOUR')
elif(digit==5):
    print('FIVE')
elif(digit==6):
    print('SIX')
elif(digit==7):
    print('SEVEN')
elif(digit==8):
    print('EIGHT')
elif(digit==9):
    print('NINE')
else:
    print('please give 1 to 9 nonly')
'''

# Iterative Statements
'''
s = "Sunny Leone the Bitch"
for x in s:
    print(x)

    
list1 = [1,2,3,4,5,90]
for x in list1:
    print(x)

    
s = "Sunny Leone the Bitch"
count = 0
for x in s:
    count+= 1
print('The number of characters in the string is',count)


s = input('enter a string:')
i =0
for x in s:
    print('The character at ',i,'index is ',x)
    i += 1

    
for x in range(3):
    print('Hello')

for x in range(11):
    if(x != 0):
        print(x)

print('The odd numbers between 1 and 21')
for x in range(21):
    if(x%2 != 0):
        print(x)

print('The odd numbers between 1 and 21')
for x in range(1,21,2):
    print(x)

for x in range(10,0,-1):
    print(x)

    
list2 = eval(input('Enter a list:'))
sum = 0
for x in list2:
    sum += x
print('The sum is ',sum)
'''

# while loop
'''
x = 1
while (x<=10):
    print(x)
    x += 1

    
x = 0
sum=0
while(x<=100):
    sum += x
    x += 1
print('The sum of first 100 numbers is :',sum)


name = ''
pwd = ''
while(name != 'Durga' or pwd !='python'):  ## we have used 'or' means if one condition fails it woll not work
    name = input('Enter a name:')
    pwd = input('Enter password ')
print('Hello Durga! thanks for conformation')



for i in range(4):
    for j in range(4):
        print('i = %d and j = %d' %(i,j))
'''

# pattern programms
'''
n = int(input('Enter number of rows:'))
for i in range(1,n+1):
    for j in range(1,i+1):
        print('*',end=" ")
    print()

       
n = int(input('Enter number of rows:'))
for i in range(n):
    print('* '*n)


n = int(input('Enter number of rows:'))
for i in range(1,n+1):
    for j in range(n+1-i):
        print('*',end=' ')
    print()
'''


# Break, Continue and pass statements.
'''
i=0
while True:
    print('Hello!')
    i += 1
    if(i==5):
        break


cart = [104,50,60,70,90,600,780,900]
for item in cart:
    if(item > 500):
        print('Sorry we cannot process the item')
        break
    print('Processing Item:',item)


for i in range(10):
    if(i%2 == 0):
        continue
    print(i)


cart = [104,50,60,70,90,600,23,45,780,56,78,900]
for item in cart:
    if(item > 500):
        print('Sorry we cannot process the item:',item)
        continue
    print('Processing Item:',item)


numbers = [10,20,0,5,0,30]
for n in numbers:
    if(n == 0):
        print('We cannot proceed this divisio since denominator = %d' %n)
        continue
    print("100/%d is %d" %(n,100/n))
'''

# String Data Type
'''
st = input('Enter a string here:')
i =0
for x in st:
    print('The letter  at positive index %d and negative index %d is %s' %(i,i-len(st),st[i]))
    i += 1


s = """Durga
Software Solutions
Private Limited"""
n = len(s)
i = 0
print('Forward Direction:')
while(i<n):
    print(s[i],end='')
    i += 1

print()
print()

print('backward direction:')
j = -1
while(j>=-n):
    print(s[j],end='')
    j -= 1


s = input('Enter your string here:')
subs = input('Enter your substring here:')

if subs in s:
    print(subs,'Substring is found in main string.')
else:
    print(subs,'Substring is not found in main string.')



s1 = input('Enter first string:')
s2 = input('Enter second string:')
if(s1<s2):
    print('First string is smaller than second string.')
elif(s1>s2):
    print('First string is bigger than second string.')
elif(s1==s2):
    print('Both strings are equal.')
else:
    print('Both strings are not comparable to each other.')


s = input('Enter a string here:')
subs = input('Enter a substring:')

flag = False
pos = -1
n = len(s)
while True:
    pos = s.find(subs,pos+1,n)
    if pos == -1:
        break
    print('Found at the index:',pos)
    flag = True
if flag == False:
    print('Not found')



s = input('Enter a string here:')
if s.isalnum():
    print("Alphanumeric characters ")
    if s.isalpha():
        print('Alphabet characters')
        if s.islower():
            print('All characters are lowercase')
        else:
            print('Uppercase characters')
    else:
        print('It is digit')
elif s.isspace():
    print('Space characters')
else:
    print('Non space special charcter')



name = "subham"
age = 26
salary = 5000
print("{}'s age is {} and his salary is: {}".format(name,age,salary) )
'''

# Some problems on Strings
'''
"""To reverse a string"""
s = 'Durga'
print(s[::-1])

for x in reversed(s):
    print(x,end='')

print()

i = len(s) - 1
output = ''
while i>=0:
    output += s[i]
    i -= 1
print(output)

"""Program to reverse each content of each word of string"""

s = input('Enetr a string')
l = s.split()
i = len(l)-1
l1 = []
while i>=0:
    l1.append(l[i])
    i -= 1
output = ' '.join(l1)
print(output)

l2 = []
for x in l:
    l2.append(x[::-1])
result = ' '.join(l2)
print(result)



"""WAP to print characters present at odd and even position for the given string"""

s = input('Enter a string:')
print('The characters at even positions are:',s[::2])
print('The characters at odd positions are:',s[1::2])

i =0
print('The characters at even position are:')
while i<len(s):
    print(s[i],end=',')
    i += 2
print()
i =1
print('The characters at odd positions are:')
while i<len(s):
    print(s[i],end=',')
    i += 2 



"""WAP to merge characters of two strings into a single string by taking characters alternatively """

s = input('Enter a string here:')
s1 = s2 = output = ''
for x in s:
    if x.isalpha():
        s1 += x
    else:
        s2 += x
for y in sorted(s1):
    output += y
for y in sorted(s2):
    output += y

print(output)



s = input('Enter the string:')
output= ''
for x in s:
    if x.isalpha():
        output += x
        previous = x
    else:
        output += previous*(int(x)-1)
print(output)
print(s)



s = input('Enter the string here:')
output = ''
for x in s:
    if x.isalpha():
        output += x
        previous = x
    else:
        output += chr(ord(previous) + int(x))
print(output)



s1 = input('Enter first string:')
s2 = input('Enter second string:')

output = ''
i=j=0
while i<len(s1) or j<len(s2):
    if i<len(s1):
        output += s1[i]
        i += 1
    if j<len(s2):
        output += s2[i]
        j += 1
print(output)


"""WAP to remove duplicate elements from the string"""

s = input('Enter a string:')
l = []
for x in s:
    if x not in l:
        l.append(x)
result = ''.join(l)
print(result)



"""WAP to count the number of occurences of characters in a string"""

s = input('Enter a string here:')
dict1 = {}

for x in s:
    if x not in dict1.keys():
        dict1[x] = 1
    else:
        dict1[x] += 1
for x,y in dict1.items():
    print('{} occurs : {} times in the string'.format(x,y))
'''

# Basic Data Structure(List,Tuple,set,dictionary)

# List Data Structure

'''
l = eval(input('Enter a list here:'))
i = 0
while i<len(l):
    print(l[i],end=' ')
    i += 1


l = [1,2,3,4,5]
x = len(l)

for i in range(x):
    print(l[i] ,'is available at +ve index',i, 'and at -ve index',(i-x))
    i += 1


l = [10,20,30,40,50,60,40]
target = int(input('Enter a value :'))
if target in l:
    print(target, 'is available in list at index:',l.index(target))
else:
    print(target,'is not available in thr list')


l = [10, 20, 30, 40, 50, 60, 70, 90, 100]
sum = 0
for x in l:
    if x<=100 and x%10 == 0:
        sum += x
print('The sum is :',sum)


l = []
for x in range(10,101):
    if(x%10 == 0):
        l.append(x)
print(l)

l.insert()



m = [[1,2,3],[4,5,6],[7,8,9]]
for i in range(len(m)):
    for j in range(len(m[i])):
        print(m[i][j],end=' ')
    print()


##################List Comprehensions####################

s = [x*x for x in range(1,21) if x%2 == 0]
print(s)

l = [2**x for x in range(1,11)]
print(l)

m = [x*x for x in range(1,21) if x%2 != 0]
print(m)

n1 = [10,20,30,40,50]
n2 = [20,30,40,50,60,70]
n3 = [x for x in n1 if x not in n2]
print(n3)


w = "the quick brown fox jumps over the lazy dog".split()
print(w)
l = [[x.title(),len(x)] for x in w]
print(l)


"""WAP to display unique vowels present in the given word"""

vowels = ['a','e','i','o','u','A','E','I','O','U']
word = input('Enter a word:')
found = []
for letter in word:
    if letter in vowels:
        if letter not in found:
            found.append(letter)
print(found)
print('The number of different vowels present in ',word,'are: ',len(found))
'''

#Tuple Data Structure
'''
t = eval(input('Enter the tuple characters:'))
sum = 0
for x in t:
    sum += x
print('The sum is:',sum)
print('The average is:',(sum/len(t)))
'''
#set Data structure

'''
l = eval(input('Enter some elements:'))
s = set(l)
l1 = list(s)
print(l1)


vowels = {'a','e','i','o','u'}
w = input('Enter some words:')
s = set(w)
d = s.intersection(vowels)
print('Vowels present in the word sre:',d)
'''


#Dictionary Data Structure
'''
rec = {}
n = int(input('Enter number of students:'))
i = 1
while i<=n:
    name = input('Enter the Name:')
    marks = input('Enter % of marks:')
    rec[name] = marks
    i += 1
print('The Name and marks are respectively:')
for x in rec:
    print(x,'\t','-','\t',rec[x]) 
while True:
    name = input('Enter Student Name to get marks:')
    marks = d.get(name,-1)
    if marks == -1:
        print('Student not found')
    else:
        print('The marks of {} : {}'.format(name,marks))  

        

d = {100: 'durga', 101: 'hello', 102: 'solutions', 103: 'solutions', 104: 'ravi'}
for k,v in d.items():
    print(k,'\t',v)



d= eval(input('Enter dictionary:'))
s = sum(d.values())
print('The sum is :',s)


w = input('Enter a word')
vowels = {'a','e','i','o','u','A','E','I','O','U'}
d = {}
for x in w:
    if x in vowels:
        d[x] = d.get(x,0) + 1
for k,v in sorted(d.items()):
    print(k,'occured ',v,'times')
'''


# Functions, packages and Modules

# Functions
'''
def wish(name):
    print("Hello",name,"Good Evening!")
    
wish('Rishy')
wish('Sumit')


def square(x):
    print('The square of {} is {}'.format(x,x*x))

square(10)
square(5)

def add(a,b):
    return a+b

print('The sum is :',add(50,150))

def even_or_odd(num):
    if num % 2 == 0:
        print('{} It is even'.format(num))
    else:
        print('{} is odd'.format(num))

print(even_or_odd(5))
even_or_odd(10.5)
even_or_odd(89)


def fact(n):
    result = 1
    while n>=1:
        result *= n
        n = n - 1
    return result

for i in range(1,6):
    print('The factorial of {} is {}'.format(i,fact(i)))


def calc(a,b):
    sum = a+b
    sub = a-b
    multi = a*b
    div  = a/b
    return sum,sub,multi,div

t = calc(5,6)
print(t)
for x in t:
    print(x)


def wishes(marks,age,name = 'Guest',msg = 'Good Morning!'):
    print('Student Name:: ',name)
    print('Student Age:: ',age)
    print('Student Marks::',marks)
    print('Message::',msg)

wishes(100,age=34)



def sum(name,*n):
    result = 0
    for x in n:
        result += x
    print('The sum by',name, ' is :',result)

sum('Durga')
sum('Anil',10)
sum('Vishesh',10,20,30,40,50,50.50)


def rec(**kwargs):
    print("The record information is :")
    for k,v in kwargs.items():
        print(k,'-----',v)

rec(name='Durga',profession = 'Teaching',location='Hyderabad',specialization = 'python')


a = 10
def f1():
    global a
    a = 60
    print('f1---',a)

def f2():
    print('f2---',a)

f1()
f2()


def f1():
    global a
    a = 60
    print('f1---',a)

def f2():
    global a
    a = 70
    print('f2---',a)

def f3():
    print('f3---',a)

def f4():
    a = 1000
    print('f4---',a)

f1()
f2()
f3()
f4()


a = 10
def f1():
    a = 100
    print(a)
    print(globals()['a'])  #to call the global value we have to use global() keyword

f1()


def fact(n):
    if n == 0:
        result = 1
    else:
        result = n*fact(n-1)
    return result

print(fact(5))
print(fact(0))



s = lambda n : 2**n
print('2 to the power of input {} is {}'.format(4,s(4)))

m = lambda a,b : a if a>b else b
print("The greatest of {} and {} is {}".format(5,6,m(5,6)))

def iseven(x):
    if x%2 == 0:
        return True
    else:
        return False
    
l = [1,2,3,4,5,6,7,8,9,10]
l1 = list(filter(iseven,l))
print(l1)


l1 = list(filter(lambda x:x%2==0,l))
print(l1)

l2 = list(filter(lambda x:x%2!=0,l))
print(l2)

def double(x):
    return 2*x

l = [1,2,3,4,5,6]
L = [5,4,3,2,1,0]
l1 = list(map(double,l))
print(l1)

l2 = list(map(lambda x:2*x,l))
print(l2)

l3 = list(map(lambda x,y : x*y,l,L))
print(l3)


from functools import reduce


l = [10,20,30,40,50]
result = reduce(lambda x,y : x+y,l)

print(result)

def wish(name):
    print('Hello {} : Good Morning'.format(name))
greeting = wish

wish('Gautam')
greeting('Rishabh')


def outer():
    print('This is outer functoin')
    def inner1():
        print('This is inner function')
    inner1()

outer()


def f1():
    def inner(a,b):
        print("The sum :",a+b)
        print("the average:",(a+b)/2)
    inner(10,20)
    inner(40,50)

f1()


def decor(func):
    def inner(name):
        if name == 'Sunny':
            print('Hello Sunny Bad Morning..!')
        else:
            func(name)
    return inner

@decor
def wish(name):
    print('Hello',name,'Good Evening!')

wish('Durga')
wish('Sunny')


def smartdiv(func):
    def inner(a,b):
        if b == 0:
            print('Rascal ! how you can divide with zero')
        else:
            return func(a,b)
    return inner

        
@smartdiv
def div(a,b):
    return a/b

print(div(4,5))
print(div(4,2))
print(div(4,0))



def decor1(func):
    def inner(name):
        print('Decor1 function is executed!')
        func(name)
    return inner

def decor2(func):
    def inner(name):
        print('Decor2 function is executed!')
        func(name)
    return inner

def decor3(func):
    def inner(name):
        print('Decor3 function is executed!')
        func(name)
    return inner

@decor3
@decor2
@decor1
def wish(name):
    print('Hello',name,'Good Morning!')

wish("Durga")



def doubledecor(func):
    def inner():
        x = func()
        return 2*x
    return inner

def squaredecor(func):
    def inner():
        x = func()
        return x*x
    return inner


@doubledecor
@squaredecor
def num():
    return 10

print(num())



def mygen():
    yield 'A'
    yield 'B'
    yield 'C'
    yield 'D'
    yield 'E'
    yield 'F'

g = mygen()
for x in g:
    print(x)

def countdown(num):
    print("Start countdown")
    while(num>0):
        yield num
        num -= 1

values = countdown(5)
for x in values:
    print(x)

def firstn(num):
    n = 1
    while(n<=num):
        yield n
        n += 1

values = firstn(8)
for x in values:
    print(x)


def fibonachi():
    a,b = 0,1
    while True:
        yield a
        a,b = b,a+b

values = fibonachi()
for x in values:
    if x>200:
        break
    print(x,end=' ')
'''

#MODULES

'''
import Lohanmath
from Lohanmath import *
print(Lohanmath.x)

add(10,100)
product(10,30)


import module1
import module1
import module1
print('This is test module.')


x = 10
y = 20
def f1():
    print('hello')

print(dir())
print(dir(module1))

print(__builtins__)
print(__cached__)
print(__doc__)
print(__file__)
print(__loader__)
print(__name__)
print(__package__)

def f1():
    if __name__ == '__main__':
        print('The code executed directly as a program.')
        print('The value of __name__ :',__name__)
    else:
        print('The code executed indirectly as a module from some other program.')

f1()



from math import *

print(sqrt(100))
print(ceil(10.1))
print(floor(10.1))
print(fabs(-10.6))
print(fabs(10.6))
print(sin(100))


from random import *

print('Random Integer values:')
for i in range(11):
    print(randint(1,20))

print('Random float values:')
for i in range(12):
    print(uniform(1,20))

print('Randrange function')
for i in range(20):
    print(randrange(10,100,5))

from random import *

l = [1,2,3,4,4,5,5,6,7]
for i in range(10):
    print(choice(l))

"""WAP to give a 6 digit OTP as output"""
for i in range(10):
    print(randint(100000,999999))
'''



