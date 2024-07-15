class A():
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
    def display(self):
        print(self.name, self.age, self.gender)
class B(A):
    def __init__(self,name,age,gender):
        A.__init__(self,name,age,gender)
class C(B):
    def __init__(self,name,age,gender):
        B.__init__(self,name,age,gender)
x=C('neelu',24,'female')
x.display()

