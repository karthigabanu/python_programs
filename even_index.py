a=input("enter a value:")
b=''
for i in range(len(a)):
    if i%2==0:
        b=b+a[i]
print(b)
