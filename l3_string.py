line='abcdefghbc'
print('line=',line)
ln=len(line)
#print('len of line %s. len+1=%s'%(ln,9))
print(line[2:4])
print(line[:3])
print(line[-3:])
print(line[6:2:-2])
print(line.find('bc',2))
print(line.count('bc'))

line=input()
print(line[2])
print(line[-2])
print(line[:5])
print(line[:-2])
print(line[::2])
print(line[1::2])
print(line[::-1])
print(line[::-2])
print(len(line))

s=input()
slist=s.split()
i=1
for w in slist[5:10]:
    print(i,w)
    i=i+1
for i,w in enumerate(slist[5:10]):
    print(i,w)
a= 'ds,as,d'.split(',')
print(a)
