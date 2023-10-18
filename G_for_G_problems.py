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
"""





