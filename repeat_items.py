#Python program to find the repeated items of a tuple.
a=(2,4,6,1,3,5,8,7,3,1,0)
l=[]
for x in a:
    if a.count(x)>1:
        l.append(x)
print(set(l))
        
