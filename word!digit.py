n=str(input('enter the string: '))
l=[]
for i in n:
    if not i.isdigit():
        l.append(i)
print(*l,sep="")
