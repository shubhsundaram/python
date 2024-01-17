"""
# code to reverse each word.
s = input('Enter a string : ')
l = s.split()
l1 = []
i = 0
while i < len(l):
    l1.append(l[i][::-1])
    i += 1
output = ' '.join(l1)
print(output)


# program to merge characters of 2 strings into a single string by taking charaters alternatively.
s1 = input("Enter a string : ")
s2 = input("Enter a string : ")

i,j = 0,0
output = ''
while i < len(s1) or j < len(s2):
    if i < len(s1):
        output += s1[i]
        i += 1
    if j < len(s2):
        output += s2[j]
        j += 1
print(output)


# write a program to sort the characters of the string and its alphabet symbols are followed by numeric values.
s = input("Enter a string here : ")
s1 = s2 = ''
for x in s:
    if x.isalpha():
        s1 += x
    if x.isdigit():
        s2 += x
    
output = sorted(s1)+sorted(s2)
output = ''.join(output)
print(output)


s = input("Enter a string here : ")
output = ''
for x in s:
    if x.isalpha():
        output += x
        previous = x
    else:
        output += previous*(int(x)-1)        
        
print(output)
        
"""


# List matrix
list1 = [[1,2,3],[4,5,6],[7,8,9]]
for i in range(len(list1)):
    for j in range(len(list1[i])):
        print(list1[i][j],end=' ')   
    print()    

