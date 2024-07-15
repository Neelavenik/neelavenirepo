def New():
    class Person_info(object):
        def __init__(self,name,age,salary):
            self.name=name
            self.age=age
            self.salary=salary
        def show(self):
            print(f'{self.name},{self.age},{self.salary}')

    return Person_info
v1=New()('neelu',25,1000)
v1.show()