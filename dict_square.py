l1=list(map(int,input('enter the keys: ').split()))
l2=[]
d={}
for i in l1:
    l2.append(i*i)
for j in range(len(l1)):
    d.update({l1[j]:l2[j]})
print(d)
