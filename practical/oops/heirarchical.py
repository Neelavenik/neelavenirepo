class Parent:
    def say(self):
        print("Hello Good Morning:")
class child1(Parent):
    def say(self):
        super().say()
        print("Gayu")
class child2(Parent):
    def say(self):
        super().say()
        print("Neelu")
class child3(Parent):
    def say(self):
        super().say()
        print("thanvi")
obj=child3()
obj.say()
obj1=child2()
obj1.say()
obj2=child1()
obj2.say()
