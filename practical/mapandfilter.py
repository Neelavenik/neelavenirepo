# l1=['neelu','gayu','thanu','bhavya']
# print(list(map(tuple,l1)))
# # for i in enumerate(l1):
# #     print(i)
# number1=[1,2,3,4,5]
# number2=[6,7,8,9,10]
# # result=map(lambda x,y:x+y ,number1,number2)
# # print(list(result))
# result=map(lambda x,y:y-x ,number1,number2)
# print(list(result))
###filter method helps to filter the sequence and displays the output
l1=[1,2,3,4,5,6,7,8,9]
# result=filter(lambda x:x%2==0,l1)
# print(list(result))
# print(list(filter(lambda x: x%2==0 ,l1)))
for i in enumerate(l1,10):
    if (list(i)[1])%2==0:
        print(list(i))

