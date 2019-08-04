#takes a sequence of numbers and determines if all the numbers are different from each other
a=[1,5,3,7,9,3]
if len(a) == len(set(a)):
    print("true")
else:
    print("false")
