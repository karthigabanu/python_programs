# Program to check the leap year
a=int(input("year:"))
if a%4==0 and a%400==0:
    print("it is a leap year")
else:
    print("not a leap year")
#output:
#year:2000
#it is a leap year
