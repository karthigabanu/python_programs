#program that will return true if the two given integer values are equal or their sum or difference is 5.
def a(x,y):
    if x == y or abs(x-y) == 5 or (x+y) == 5:
        return True
    else:
        return False
print(a(2,3))
print(a(8,3))
print(a(4,3))

   
