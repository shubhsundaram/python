"""
print("Please enetr two numbers here.")
print("(type 'q' if you want to quit)")
while True:
    first_num = input("Enter the first number : ")
    if first_num == 'q':
        break
    second_num = input("Enter second number : ")
    try:
        answer = int(first_num)/int(second_num)
    except ZeroDivisionError:
        print('Sorry! You cannot divide something by 0')
    else:
        print(answer)


def count_words(filename):
    #This function wil count the number of words in a file.
    try:
        with open(filename) as file_object:
            content = file_object.read()
    except FileNotFoundError:
        print("Sorry, this fils is not avai;ab;e in the directory.")
    else:
        words = content.split()
        print("The file "+filename+" has"+str(len(words))+" words stored in it.")
        
count_words('alice.txt')

filenames = ['alice.txt','siddhartha.txt','moby_dick.txt','little_women.txt']
for filename in filenames:
    count_words(filename)


while True:
    first_num = input("Enter first numebr : ")
    if first_num == 'q':
        break
    second_num = input("Enter second numebr :")
    try:
        addition = int(first_num) + int(second_num)
    except ValueError:
        print("Sorry, you cannot add a string and an integer.")
    else:
        print(addition)


with open('cats.txt','w') as file_object:
    file_object.write('Meloni\n')
    file_object.write('katrina\n')
    file_object.write('sweety')
    
with open('dogs.txt','w') as file_object:
    file_object.write('Bob\n')
    file_object.write('Rock\n')
    file_object.write('Jumanji')

try:
    with open('cats.txt') as file_object:
        content_cat = file_object.readlines()
    with open('dogs.txt') as file_object:
        content_dog = file_object.readlines()
except FileNotFoundError:
    print("Sorry,this file is not available at the moment.")
    # if you want to print nothing in except block then just pass here.
else:
    print("The cats are : \n")
    for cat in content_cat:
        print(cat)
        print()
    print("The dogs are : \n")
    for dog in content_dog:
        print(dog)
"""

