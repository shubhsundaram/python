# Time and Efficiency of code
"""
import time
start = time.time()
for i in range(1,101):
    print(i)
print('time to execute this is :',time.time() - start)

j = 1
while j<101:
    print(j)
    j += 1
print('time to execute this is :',time.time() - start)
''' time to execute both programs differes.'''


# problem - 1
l = [1,2,3,4,5,6]
sum = 0
for i in l:
    sum += i
print('The sum is : ',sum)

product = 1
for i in l:
    product *= i
print('The product is : ',product)
''' order of complexity of first loop is O(n) and that of second loop is also O(n)
so, O(n) + O(n) == O(n) '''

# problem- 2
l1 = [1,2,3,4,5]
for i in l1:
    for j in l1:
        print('({},{})'.format(i,j))
''' O(n)*O(n) == O(n^2) i.e Quadratic'''

'''Note : The O(n) of linear search is linear.'''

# problem - 3
def inToStr(i):
    digits = '0123456789'
    if i == 0:
        return '0'
    result = ''
    while i > 0:
        result = digits[i%10] + result
        i = i//10
    return result
'''if i == 1234 then the loop will be iterating 4 times and so on. hence, it it logarithmic order '''

'''Note : The Binary Search is log(n)''' 

# problem - 4
A  = [1,2,3,4]
B = [2,3,4,5]

for i in A:
    for j in B:
        for k in range(100000):
            print('({},{})'.format(i,j))
''' Here, the output of third loop is constant i.e does not depend on the input.so,
    O(n)*O(n)*O(1) == O(n^2) i.e quadratic'''


# problem - 5
L = [1,2,3,4,5]

for i in range(0,len(L)//2):
    other = len(L) - i - 1
    temp = L[i]
    L[i] = L[other]
    L[other] = temp
print(L)
'''here O(n/2) == O(n)'''
'''Note: the order of complexity for the recursion is O(n)'''

# problem - 6
def fib(n):
    if n == 1 or n == 0:
        return 1
    else:
        return fib(n-1) + fib(n-2)
''' the Order of complexity is exponential here in fibonaci series.'''
'''Note : whenever there is s dividion it means there the pattern is logarithmic'''


# problem - 7
def sum_digits(num):
    sum = 0
    while(num>0):
        sum += num % 10
        num /= 10
    return sum
'''The order of complexity is logarithmic here.'''


import sys

L = []
for i in range(100):
    print(i,sys.getsizeof(L))
    L.append(i)
"""

#############  python Dynamic Array   ##################

import ctypes

class Mylist:

    def __init__(self):
        self.size = 1
        self.n = 0
        self.A = self.__make_array(self.size)

    def __len__(self):
        return self.n
    
    def append(self,item):
        if self.n == self.size:
            self.__resize(self.size*2)
        self.A[self.n] = item
        self.n += 1
    
    def __resize(self,new_cpapcity):
        B = self.__make_array(new_capacity)
        self.size  new_capacity
        
    def __make_array(self,capacity):
        return (capacity*ctypes.py_object)()