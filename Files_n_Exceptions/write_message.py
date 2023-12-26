"""
filename = 'programming.txt'


with open(filename,'w') as file_object:
    file_object.write("I love to code on python.\n")
    file_object.write("i am fully aware of what i am writing here.\n")

with open(filename,'a') as file_object:
    file_object.write("also i want to add some of my views on the for loop here :\n")
    file_object.write("for loop is very essential in part of programming life as it can iterate over as many items as possible is a list.")
"""

filename = 'guest_book.txt'
while True:
    user = input("Enter you name here :\n")
    with open(filename,'a') as file_object:
        file_object.write(user+'\n')