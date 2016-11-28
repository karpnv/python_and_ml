a=[1,2,3,4,12,11,'a','b','abc']

b1={1,2,3,4,2,1,'a','a'}
b=set(a)
# print('a ',a)
# print(b>b1)
a.append('d')
print(b)
b=b|{'b','d'}
print(list(b))
# for elem in a:
#     print(elem)
#print(10 in b)