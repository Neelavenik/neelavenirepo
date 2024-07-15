from module1 import *
n=eval(input("enter a number:"))
if n==1:
    print(add(a=int(input("enter a number:")),b=int(input("enter another number:"))))
elif n==2:
    print(sub(a=int(input("enter a number:")),b=int(input("enter another number:"))))
elif n == 3:
    print(prod(a=int(input("enter a number:")), b=int(input("enter another number:"))))
elif n == 4:
    print(div(a=int(input("enter a number:")), b=int(input("enter another number:"))))
elif n == 5:
    print(modulodiv(a=int(input("enter a number:")), b=int(input("enter another number:"))))
else:
    print("invalid input")




