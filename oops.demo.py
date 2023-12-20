from oops import calculator

class childimpl(calculator):
    num2 =200
    def __init__(self):
        calculator.__init__(self,35,50)
    def getcompdata(self):
        return self.num + self.num2 + self.summation()



obj=childimpl()
print(obj.getcompdata())

