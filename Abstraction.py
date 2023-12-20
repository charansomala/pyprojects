# ABstraction refers to the concept of hidding complex implementation deatils and showing only the essential features of an
# obj or func. it allows u to focus on what an obj does rather than how its acheived its funcationalty.
class car():
    def __init__(self,make,model):
        self.make = make
        self.model = model

    def start_engine(self):
        raise notImplentationError("sub class must implement the start_enginemethod")


my_car = car("Audi","Q5")

my_car.start_engine()
#trying to start the engine     (ABSTRACT METHOD)
# in this ex the car class has an abstract method start engine when u
# create a instance of a car class and try to start the engine it raises
# a not implemented error this enforces that any subclass of a car must
# provide its own implementation of the start engine method  promoting
# abstraction by hiding the specific engine starting details at the superclass level

