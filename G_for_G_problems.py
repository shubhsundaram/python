################  LIST  ###################
# Basic List Programs
"""
''' Python program to interchange first and last elements in a list '''
def swapnum(list):
    size = len(list)
    temp = list[0]
    list[0] = list[size-1]
    list[size-1] = temp

    return list
list = [1,2,3,4,5]
print(swapnum(list))

''' Python Program to Swap Two Elements in a List '''
def swappos(list,pos1,pos2):
    # shift pos1 with pos2
    list[pos1],list[pos2] = list[pos2],list[pos1]

    return list
list = [10,20,30,40,50]
print(swappos(list,1,3))

''' Find Maximum of two numbers in Python'''
def max(a,b):
    if a>= b:
        return a
    else:
        return b
a,b = 5,6
print(max(a,b))

'''Python Program to find sum and average of List in Python'''
list1 = [1,2,3,4,5,6,7]
def sumnavg(list1):
    x = len(list1)
    sum = 0
    for n in list1:
        sum += n
    print('The sum is : ',sum)
    for m in list1:
        avg = sum/x
    print('The average is :',avg)
print(sumnavg(list1))


''' Python | Sum of number digits in List '''
list1 = [12,23,34,45,56,67,78]
list2 = []
for n in list1:
    sum = 0
    while(n!=0):
          rem = n % 10
          sum += rem
          n = n//10
    list2.append(sum)
print(list2)

''' Python | Multiply all numbers in the list '''
list1 = [1,2,3,4,5,6,7]
mul = 1
for n in list1:
     mul = mul*n
print('The product of all the elements in the list is : ',mul)
     

''' Python program to find smallest and largest number in a list '''
list1 = [3,4,1,3,9,10,560]
list1.sort()
print('The smallest number in the list is : ',list1[0])
print('The largest number in the list is : ',list1[-1])
print('The second largest number in the list is : ',list1[-2])


''' Python program to print even numbers in a list '''
list1 = [3,4,1,3,9,10,560,6,8,1,11,13,15,16]
list2 = []
list3 = []
def evennodd(list1):
    for n in list1:
        if n%2 == 0:
            list2.append(n)
        else:
            list3.append(n)
    print('The odd number list is : ',list3)
    print('The even number list is : ',list2)
print(evennodd(list1))


''' Python program to print all even and odd numbers in a range '''
l1 = []
l2 = []
a = b = 0
for i in range(1,150):
    if i%2==0:
        l1.append(i)
        a += 1
    else:
        l2.append(i)
        b += 1
print('The even numbers in the range are :')
print(l1)
print('The total even numbers in the range are : {}'.format(a))
print('The odd numbers in the range are :')
print(l2)
print('The total odd numbers in the range are : {}'.format(b))

''' Python program to print positive and negative numbers in a list '''
list1 = [1,-2,-3,4,5,6,-9,-10,11,0,20]
print('The positive numbers in the list are : ')
for x in list1:
    if x>0:
        print(x,end=',')
print()
print('The negative numbers in the list are : ')
for x in list1:
    if x<0:
        print(x,end=',')

''' Python program to print all negative numbers in a range '''
for i in range(-19,200):
    if i<0:
        print(i,end=',')

''' Python program to remove empty tuples from a list of tuples '''
def remove(tuple):
    for i in tuple:
        if len(i) == 0:
            tuple.remove(i)
    return tuple
tuple = [(),('ram','sita'),(3,4,5)]
print(remove(tuple))

''' Python | Program to print duplicates from a list of integers '''
list1 = [1,2,3,4,5,6,7,8,9,1,1,5,6,8,8,10,10,3,3]
uniquelist  = []
duplicatelist  = []
for i in list1:
    if i not in uniquelist:
        uniquelist.append(i)
    elif i not in duplicatelist:
        duplicatelist.append(i)
print(duplicatelist)
"""

################  STRINGS  ###################
# Basic Strings Programs
"""
''' Python program to check whether the string is Symmetrical or Palindrome '''
string = "malayalam"
s = string[::-1]
if s==string:
    print('Palindrome string')
else:
    print("Not a palindrome string")

''' Reverse Words in a Given String in Python '''
str1 = 'geeks quiz practice code'
l = str1.split()[::-1]
str2 = ' '.join(l)
print(str2)


''' to remove i'th character from string in Python '''
s = 'Hello happy python learning !'
s1 = s.replace('n','')   # replace nothing in place of n
print(s1)

''' To Avoid Spaces in string length '''
s2 = s.replace(' ','')
print(s2)
print('The total characters without spaces in the string are : ',len(s2))


''' Python program to print even length words in a string '''
str1 = 'Hey how are you geeks are you doing good at it !'
l = str1.split()
print('The even length words are : ')
print()
for word in l:
    if len(word) % 2 == 0:
        print(word,end=' ')


''' To Uppercase Half String '''
str1 = 'Hey how are you geeks are you doing good at it !'
half_size = len(str1)//2
res = ''
for i in range(len(str1)):
    if i<=half_size:
        res += str1[i].upper()
    else:
        res += str1[i]
print('The new modified string becomes : ',res)


''' Python program to capitalize the first and last character of each word in a string'''
str1 = 'Hey how are you geeks are you doing good at it'
l = str1.split()
l2 = []
for word in l:
    x = word[0].upper() + word[1:-1] + word[-1].upper()
    l2.append(x)
str2  = ' '.join(l2)
print(str2)


''' Python program to check if a string has at least one letter and one number'''
s = 'serm'
res = s.isdigit() and s.isalpha()
print(res)


''' Program to accept the strings which contains all vowels '''
string = input('Enter a string here : ')
def check(string):
    if len(set(string.lower()).intersection('aeiou')) >=5 or len(set(string.upper()).intersection('AEIOU')) >=5:
        return 'accepted'
    else:
        return 'not accepted'

print(check(string))


''' Count the Number of matching characters in a pair of string'''
s1 = "hello...!! there my name is subham lohan and i am learning python"
s2 = "hey...!! i am Amitesh and grasping the concepts of Django right now"
s3 = s1.replace(' ','')
s4 = s2.replace(' ','')
l = []
for char in s3:
    if char not in l:
        if char in s4:
            l.append(char)
print(l)
print('The number of matching characters in both strings are : ',len(l))


''' Python program to count number of vowels using sets in given string '''
vow = ['a','i','e','o','u','A','E','I','O','U']
str1 = "Hello there "
s1 = set(str1)
inters = s1.intersection(vow)
print('The number of vowels present in the string are : ',len(inters))


''' Python Program to remove all duplicates from a given string '''
str1 = "Hello buddy I think you are stuck somewhere in the process..Go ahead"
i = 0
str2 = ''
for i in str1:
    if i not in str2:
        str2 += i
str3 = str2.replace(' ','')
print('The string becomes : ',str3)


''' Least Frequent and most frequent Character in String '''
from collections import Counter
str1 = "Hello How are You dear "
res = Counter(str1)
res1 = Counter(str1)
res = min(res,key = res.get)
res1 = max(res1,key = res1.get)
print('The minnimum of all the characters in the string is : ', str(res))
print('The maximum of all the characters in the string is : ', str(res1))


''' Odd Frequency Characters '''
from collections import Counter
str1 = "Hello How are You dear "
res = Counter(str1)
res = [key for key,value in res.items() if value % 2 != 0]
print('The odd frequency characters are : ',str(res))
"""

''' Specific Characters Frequency in String List
from collections import Counter
str1 = "Hello How are You dear...!! "
res = Counter(str1)
res = [key for key,value in res.items() if value % 2 != 0]
print('The odd frequency characters are : ',str(res))
'''
