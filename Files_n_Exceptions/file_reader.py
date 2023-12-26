"""
# this is how we open text file if the text file is stored somewhere.
file_path = 'C:/Users/Subham Lohan/OneDrive/Desktop/python_Tuts/Files_n_Exceptions/pi_digits.txt'
with open(file_path) as file_object:
    contents = file_object.read()
    print(contents)
    
# This is the way to print the text file if the text file is stored in the same directory.
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents)


# To read a file line by line and print it.
with open('pi_digits.txt') as file_object:
    for line in file_object:
        print(line.rstrip())


with open('pi_digits.txt') as file_object:
    lines = file_object.readlines()
    
pi_string = ''
for line in lines:
    pi_string += line.strip()
    
print(pi_string)
print(len(pi_string))
"""

  
    

    
