a=input("enter a string")
r=''
for i  in a:
    r=i+r
if r==a:
    print("palindrome")
else:
    print("not a palindrome")
