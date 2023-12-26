import json
"""
def favorite_num():
    filename = 'number.json'
    try:
        with open('number.json') as file_object:
                number = json.load(file_object)
        print("I know your favorite number! It's "+str(number)+".")
    except FileNotFoundError:
        number = int(input("Enter your favorite number here : "))
        with open('number.json','w') as file_object:
            json.dump(number,file_object)
    else:
        print("We'll remember your favorite number buddy..!")
        
            
favorite_num()

"""

def get_stored_user():
    filename = 'username.json'
    try:
        with open(filename) as file_object:
            username = json.load(file_object)
    except FileNotFoundError:
        return None
    else:
        return username
    
def greet_user():
    username = get_stored_user()
    print(username+"\n")
    print("Is this the correct usrname.\n")
    ask_user = input("(type 'yes' or 'no') : ")
    if ask_user == 'yes':
        print("Welcome back "+username+".")
    else:
        username = get_new_user()
        print("we'll remember you "+username+" ..!")

def get_new_user():
    username = input("Enter your name here : ")
    filename = 'username.json'
    with open(filename,'w') as file_object:
            json.dump(username,file_object)
    return username
    
greet_user()

