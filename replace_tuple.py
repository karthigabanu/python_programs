#program to replace last value of tuples in a list. 
x = [(1,2,3,4,5), (6,7,8,9,0)]
a = []
for i in x: 
    y = list (i) 
    y[-1]=100 
    t= tuple(y) 
    a.append(tuple(t)) 
print (a)
