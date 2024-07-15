numbers=[2,4,5,16,25,30,36,40,49]
# from math import sqrt
# def squareroot(num):
#    return sqrt(num).is_integer()
#
# print(list(filter(squareroot,numbers)))
# def EvenNumber(num):
#     return num%2 != 0
# print(list(filter(EvenNumber,numbers)))
from functools import reduce
print(list(map((lambda y:y>2),(filter( lambda x: x%2==0,numbers)))))
print(reduce((lambda x,y:x+y) ,list(map((lambda y:y>2),(filter( lambda x: x%2==0,numbers))))))