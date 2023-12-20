class car():
    def __init__(self,make,model):
        self.__make = make                #this __ will make private attribute
        self.model = model                #this is public attribute


    def get_make(self):
        return self.__make

    def set_make(self,new_make):
        self.make = new_make

# creating an instance of the car class
my_car = car("AUDI","Q7")

# accessing public attribute
print("car model",my_car.model)
# accessing private attribute
print("car make",my_car.get_make())
# updating the setter
my_car.set_make("BMW")
# in this example model is a public attribute the class provide getter and setter methods (get_make and set_make)
# to access the modification this ensure encapsulation by hidding the implimentation details and controlling access to thre class attributes )
print("update car make",my_car.get_make())
