#concatenate following dictionaries to create a new one.
d1={"a":1,"b":2}
d2={"c":3,"d":4}
d3={}
for d in(d1,d2):
    d3.update(d)
print(d3)
