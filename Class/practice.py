
"""
class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
        
    def set_number_served(self,number):
        self.number_served = number
    
    def increment_number_served(self,increment):
        self.number_served += increment
    
    def describe_restaurant(self):
        name = 'The Restaurant name is '+ self.restaurant_name + ' ' + 'and the cuisine type is ' + self.cuisine_type
        return name
    def open_restaurant(self):
        print('The restaurant is open..!')
        

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['Vanilla','chocolate','strawberry','butter-scotch','mango']    
        
    def flavor_display(self):
        for flavor in self.flavors:
            print("Flavour : "+flavor.title())

my_icecream = IceCreamStand("The punjabi tadka","5 Star")
print(my_icecream.describe_restaurant())
my_icecream.flavor_display()


class User():
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempt = 0
        
    def increment_login_attempts(self):
        self.login_attempt += 1
    
    def reset_login_attempts(self):
        self.login_attempt = 0
    
    def describe_user(self):
        full_name = self.first_name.title()+ ' ' + self.last_name.title()
        return full_name
    
    def greet_user(self):
        print("Hello, "+ self.full_name + ' have a nice day ahead...')

class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = Privileges()
        
        
class Privileges():
    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]
    
    def show_privileges(self):
        for privilege in self.privileges:
            print("Admin "+privilege)
               

my_admin = Admin("Vanshika","Rathore")
print(my_admin.describe_user())
my_admin.privileges.show_privileges()
"""

# Inheritance in python

from bike import bike

class electric_bike(bike):
    def __init__(self,make,model,color,year):
        super().__init__(make,model,color,year)
        self.battery = Battery()

class Battery():
    def __init__(self,battery_size= 70):
        self.battery_size = battery_size
        
    def battery_description(self):
        print("This battery is "+str(self.battery_size)+" KWh size")
    
    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 90:
            range = 300
        print("This car can go upto "+str(range)+" KM range in full charge.")
    
    def upgrade_battery(self):
        if self.battery_size < 85:
            self.battery_size = 85
        
    
my_tesla = electric_bike('Tesla','A5','Blue','2023')
print(my_tesla.get_descriptive_name())
my_tesla.battery.battery_description()     # this is the way to use a class as an attribute in another class
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.battery_description()

