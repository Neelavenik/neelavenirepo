#from multipledispatch import dispatch

class  Father(object):
    fathername=""
    def father(self):
        print(self.fathername)
class Mother(object):
    mothername=""
    def mother(self):
        print(self.mothername)
class Child(Father,Mother):
    def parent(self):
        print(self.fathername,self.mothername)
baby=Child()
baby.fathername="roma"
baby.mothername="diana"
baby.parent()
