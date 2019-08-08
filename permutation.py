#create all possible permutations from a given collection of distinct number
import itertools
l=[]
l=list(map(int,input("nos:").split(',')))
print(l)
for i in itertools.permutations(l):
    print(i)
