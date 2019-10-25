def palin(s):
    if s == s[::-1]:
        print('Is a palindrome')
    else:
        print('Not a palindrome')
s=str(input('enter a string'))
palin(s)
