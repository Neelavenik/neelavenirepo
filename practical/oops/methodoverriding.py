class A:
    def __init__(self,name):
        self.name='neelu'
        print("Hello " + self.name)
class B(A):
    def __init__(self,name):
        print("Hello " + name)
        super().__init__(name)

obj=B('bhavya')


