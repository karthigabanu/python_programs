n=str(input('enter the string: '))
a=n.split() 
b=set(a)
for i in b:
    print('FRENQUENCY OF ',i,"is: ",a.count(i))
