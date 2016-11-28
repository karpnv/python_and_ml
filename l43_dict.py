d1=dict()
d1={'Russia':'Moscow','USA':'Washington'}
d1['Russia']={'sh':'Entusiastov','pr':'Lenina'}
d2=dict(zip('abcdef', list(range(6))))
c1=(1,2,'a')
d1[c1]=3
#print(d1[(1,2,'a')])
# for key in d1:
#     print(key, d1[key])
# for key,value in d1.items():
#     print(key, value)
#print(type(dict(zip('abcdef', list(range(6)))).items()))
for key,value in dict(zip('abcdef', list(range(6)))).items():
    print(key, value)
print()