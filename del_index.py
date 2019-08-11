a=[12,24,35,70,88,120,155]
c=0
for i in a:
   
   if c == 0:
       a.remove(i)
   elif c == 4:
       a.remove(i)
   elif c == 5:
       a.remove(i)
   c+=1
print(a)
