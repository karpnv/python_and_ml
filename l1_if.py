n=int(input())
k=int(input())

# if n==10:
#     print('n==10')
# elif n>10:
#     print('n>10')
# elif n<10:
#     print('n<10')

if n==10 and (k!=5):
    print('n=10 и k не равно 5')
else:
    print('блок else')

if n==10 or (not k==5):
    print('n=10 или k не равно 5')
