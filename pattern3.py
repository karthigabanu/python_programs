def p(n):
    no=1
    for i in range(1,n+1):
        for j in range(0,i):
            print(no,end=" ")
            no=no+1
        print("\r")
n=4
p(n)
