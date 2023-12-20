class employee:

    def no_of_workinghours(self):
        self.no_of_workinghours = 40

    def displaythenumberofworkinghours(self):
        print(self.no_of_workinghours)

class trainee(employee):
    def no_of_workinghours(self):
        self.no_of_workinghours = 45

    def reset_numberofworkinghours(self):
        super().no_of_workinghours()

emp =employee()
emp.no_of_workinghours()
print("Number of working hours of emps:" ,end='')
emp.displaythenumberofworkinghours()

trainee = trainee()
trainee.no_of_workinghours()
print("Number of working hours of trainee:" ,end='')
trainee.displaythenumberofworkinghours()
trainee.reset_numberofworkinghours()
print("number of working hours has been reset:" ,end='')
trainee.displaythenumberofworkinghours()