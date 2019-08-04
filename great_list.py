#test whether all numbers of a list is greater than a certain number.\
l = [28,5,17,2,20,19]
a = int(input('enter the number:'))
if a > max(l):
    print(True)
else:
    print(False)
