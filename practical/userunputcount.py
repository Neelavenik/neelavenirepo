l1=[2,3,4,5,6,7,8,9,2,3,2,4,2,4,5,4,3,3]
n=int(input("Enter a number: "))
count=0
for i in l1:
    if n==i:
         count+=1
print(count)