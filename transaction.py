netamt=0
l=[]
while True:
    a=input("enter value:")
    l=a.split(" ")
    print(l)
    typ=l[0]
    if typ=='d'or typ=='D':
        netamt+=int(l[1])
    elif typ=='w'or typ=='W':
        netamt-=int(l[1])
    else:
        break
print("net amt is %d"%(netamt))
