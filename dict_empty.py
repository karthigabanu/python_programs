#Python program to check a dictionary is empty or not
def a(d):
    if d:
        return "not empty"
    else:
        return "empty"
print(a({'a':1}))
print(a({}))
