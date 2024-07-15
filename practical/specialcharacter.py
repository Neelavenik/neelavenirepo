num=int(input("Enter a number:"))
sum=0
prod=1
sum1=0
temp=num
while num!=0:
    r=num%10
    sum=sum+r
    prod=prod*r
    num=num//10
sum1=sum+prod
print(sum,prod,sum1)
if sum1==temp:
    print("the sum of product and sum of number is equal to given number")
else:
    print("the sum of product and sum of number is not equal to given number")





