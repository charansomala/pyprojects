class calculator:
    num = 100


    def getData(self):
        print("i am now executing as method in class")
    def __init__(self,a,b):
        self.firstnumber = a
        self.secondnumber = b
        print("i will run first")

    def summation(self):
        return self.firstnumber + self.secondnumber + calculator.num




obj = calculator(35,50)
obj.getData()
print(obj.num)

print(obj.summation())


#new keyword is not required in python
#self keyword is mandatory for calling variables into names
#__init__ is a constructor
#create a child class and call the parent class create one construt