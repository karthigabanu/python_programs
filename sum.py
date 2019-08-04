# calculate the sum of three given numbers, if the values are equal then return thrice of their sum\
a=int(input("enter 1st number:"))
b=int(input("enter 2nd number:"))
c=int(input("enter 3rd number:"))
if(a==b==c):
    print(3*(a+b+c))
else:
    print(a+b+c)
