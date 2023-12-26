from collections import OrderedDict

fav_language = OrderedDict()  
# this function lets you to get an ordered dictionary as output.
fav_language = {'Rohan':'C','Sunny':'Python','Ronnie':'java','Vishnu':'Go'}
for name,language in fav_language.items():
    print(name+"'s"+" favourite language is :"+language)
    
    
from random import randint

class Die():
    def __init__(self):
        self.sides = 6
        
    def roll_die(self):
        for x in range(10):   # to roll the die 10 times we use for loop here.
            x = randint(1,self.sides)
            print("Random Number : "+str(x))

my_die = Die()
my_die.roll_die()