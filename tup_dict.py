#Python program to convert a tuple to a dictionary
t=((2, "w"),(3, "r"))
print(dict((y,x)for x,y in t))
