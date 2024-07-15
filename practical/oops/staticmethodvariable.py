#Static variables are defined within the class and outside of the instance method as
# they are not varied form object to object
#syntax classname.variablename=value
class Number:
    x=10
    def __init__(self):
        self.y=20
    @staticmethod
    def change():
     Number.z=200
num=Number()
num2=Number()
print(num.x,num.y)
print(num2.x,num2.y)
Number.x=100
print(num.x,num.y)
print(num2.x,num2.y)
num.change()