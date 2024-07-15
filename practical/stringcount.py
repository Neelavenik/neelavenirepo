# st1="cat bat mat rat fat chat"
# l1=1
# #print(str.count("at"))
# for i in str.split():
#     l1.append(i)
# print(l1)

# print(len(st1))
# for i in range(len(st1)-1):
#     if st1[i] + st1[i+1] == 'at':
#         l1 = l1 + 1
#
# print(l1)


#mini peaks
x1 = [2,3,5,6,3,6,7,8,9,3,5]

for i in range(len(x1)-2):
    if(x1[i]) < (x1[i+1]) < (x1[i+2]):
       i=i+1
       print(x1[i])




