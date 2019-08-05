#Python program to remove an item from a tuple.
t=(2,4,6,1,3,5,8,7)
print(t)
l=list(t)
l.remove(5)
t=tuple(l)
print(t)
