
class bike():
    def __init__(self,make,model,color,year):
        self.make = make
        self.model = model
        self.color = color
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        long_name = str(self.year)+' '+self.make+' '+ self.model +' '+self.color
        return long_name
    
    def get_odometer(self):
        print("This bike has covered "+str(self.odometer_reading)+' miles so far.')
        
    def increment_odometer(self,miles):
        self.odometer_reading += miles
        
    def update_odometer(self,milaege):
        if milaege >= self.odometer_reading:
            self.odometer_reading = milaege
        else:
            print("You can't roll back an odometer..!")
     
my_new_bike = bike("Bajaj","Z-pro","Black",2019)
print(my_new_bike.get_descriptive_name())

my_new_bike.update_odometer(11000)
my_new_bike.get_odometer()

my_new_bike.increment_odometer(150)
my_new_bike.get_odometer()

