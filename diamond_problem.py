class A:
    def display(self):
        print("dispaly from class A")

class B(A):



    def display(self):
        print("display from class B")


class C(A):

    def show(self):
        print("hi from c class")
    def display(self):
        print("display from class C")

class D(B,C):
    pass

    # def display(self):
    #      print("display from class D")




d=D()
d.display()
# print(D.mro())