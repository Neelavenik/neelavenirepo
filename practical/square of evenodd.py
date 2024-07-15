# r=range(1,51)
# from functools import reduce
# oddnumber=list(filter(lambda x: x % 2 != 0, r))
# print(oddnumber)
# squarenumber=list(map(lambda y: y**2 , oddnumber))
# print(squarenumber)
# sumofsquare=reduce(lambda a,b:a+b,squarenumber)
# print(sumofsquare)
# print((lambda var : ('even number') if var%2==0 else ('odd number'))(sumofsquare))
# print(------------------------)
from functools import reduce
print((lambda var :('even number') if var%2==0 else('oddnumber'))
      (reduce(lambda a,b:a+b,list(map(lambda x:x**2 , list(filter(lambda y:y%2==0 ,
                                                                  range(1,51))))))))