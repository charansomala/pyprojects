#user defined function
def helloworld():
    print("im a function")
helloworld()
length=35
width=35
def computearea(length,width):
    area = length*width
    print(area)
computearea(20,20)

def _hello(name):
    print("HI" + name)
_hello("charan")

x = lambda a,b:a + b
print(x(10,20))