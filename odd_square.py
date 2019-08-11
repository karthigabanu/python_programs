a=list(map(int,input("enter the value: ").split(',')))
l=[]
c=0
for i in a:
    if i % 2 != 0:
        c=i*i
        l.append(c)
print(l)
