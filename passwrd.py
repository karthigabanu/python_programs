import re 
n = str(input("enter a password: "))
i= "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
a = re.compile(i)      
b = re.search(a,n) 
if b:
    print("Password is valid.") 
else:
    print("Password invalid !!")
