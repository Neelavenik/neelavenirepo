class Student:
    name='neelu'
    def __init__(self):
        Student.school="ssgv"
        print(Student.name)
        print(Student.school)
    def college(self):
        Student.clge="Nri"
        print(Student.clge)
        self.name="lavanya"
        print(self.name)

    @classmethod
    def degree(cls):
        Student.dgr="AER"
        cls.specialization="bsc"
        print(Student.specialization)
        print(Student.dgr)
    @staticmethod
    def postgraduation():
        Student.pg="Padmavathi"
        print(Student.pg)

print("------------")
s1=Student()
s1.college()
Student.degree()
Student.postgraduation()
print("=================")
s2=Student()
s2.degree()
s2.college()
s2.postgraduation()

