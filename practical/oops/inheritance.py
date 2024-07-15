class A(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(self.name, self.age)

class B(A):
    ...

ob1=B('neelu',25)

ob1.display()

