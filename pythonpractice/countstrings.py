a='neelulavanyakavyabhavya'
out=dict()
for i in a:
    k=a.count(i)
    print(f'{i}:{k}')
    out.update({i:k})
     # out[i]=k

print(out)
