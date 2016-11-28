#Работаем со списаками аналогично строкам
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
