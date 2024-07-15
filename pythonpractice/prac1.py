
num=int(input("Enter a number: "))
sum=0
temp=num
while num!=0:
    r=num%10
    sum=sum+r
    num=num//10
if temp%sum==0:
    print("niven number")
else:
    print("not niven number")
