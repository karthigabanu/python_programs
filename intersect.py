l1=[1,3,6,78,35,55]
l2=[12,24,35,24,88,120,155]
a=[]
for i in list(l1):
    if i in list(l2):
        a.append(i)
print(a)
