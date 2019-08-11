n=[12,24,35,70,88,120,155]
l=[]
for i in n:
    if i % 5 != 0 and i% 7 != 0:
        l.append(i)
print(l)       
