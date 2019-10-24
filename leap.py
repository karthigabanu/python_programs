# Program to check the leap year
a=int(input("year:"))
if ((a % 4 == 0)and (a % 100 != 0) and (a % 400 == 0)):
    print('leap year:'a)
else:
    print('not a leap year')
    
