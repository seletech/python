#Enumerate() in Python*
#python #tricks
lst = ['a','b','c','d']
obj = enumerate(lst)
print(type(obj))

for k,v in obj:
    print(k,v)
