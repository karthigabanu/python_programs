###"pattern program\
*
**
***
****
*****"""
###
def pat(n):
    l=[]
    for i in range(1,n+1):
        l.append('* '*i)
    print('\n'.join(l))
n=int(input('enter a number'))
pat(n)
