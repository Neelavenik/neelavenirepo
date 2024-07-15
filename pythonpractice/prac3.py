num=int(input("Enter a number: "))
temp=num
sum=0
i=1
while i<=num-1:
    if num%i==0:
        sum=sum+i
    i=i+1

if temp%sum==0:
    print("The number is perfect")
else:
    print("The number is not perfect")

