# program to combine two dictionary adding values for common keys
from collections import Counter
a={'a':10,'b':20,'c':30}
b={'a':5,'b':10}
d=Counter(a)+Counter(b)
print(d
