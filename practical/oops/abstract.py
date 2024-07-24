from abc import ABC, abstractmethod
class Animal(object):
    @abstractmethod
    def move(self):
        ...
    @abstractmethod
    def talk(self):
        ...
    @abstractmethod
    def eat(self):
        ...
    @abstractmethod
    def sleep(self):
        ...
    def no_of_legs(self):
        print("it has four legs")
    def color(self):
        print("it is brown in colour")
    def breeds(self):
        print("it is an indian breed")

# class Dog(Animal):
#     def move(self):
#         print("It can walk and run")
#     def talk(self):
#         print("it will bark")
#     def eat(self):
#         print("it will eat meat")
#     def sleep(self):
#         print("it will sleep")
class Cat(ABC):
    def move(self):
        print("It can walk and run")
   # def talk(self):
        #print("it sounds like meow meow")
    # def eat(self):
    #     print("it will eat rat")
    # def sleep(self):
    #     print("it will sleep under blankets")
# object=Dog()
# object.move()
# object.talk()
# object.eat()
# object.sleep()
# object.no_of_legs()
# object.color()
# object.breeds()
print("============")
object2=Cat()
object2.move()
object2.talk()
object2.eat()
object2.sleep()
