import re
txt="You're - the one who can change your life"
x=re.search('You',txt)
print(x)
y=re.findall("[a-x]",txt)
print(y)