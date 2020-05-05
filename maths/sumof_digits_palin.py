def pal(n):
    sum = 0
    while(n > 0):
        rem = n%10
        sum = sum + rem
        n = int(n/10)
    pal_check(sum)

'''def check_pal(num):
    k = s = 0
    k = num
    while(num>0):
        rem = num%10
        s = (s*10) + rem
        num = int(num/10)
    if k == s:
        print('palindrome')
    else:
        print('not')'''

def pal_check(num):
    k = rev = 0 
    k = num
    rev = str(num)[::-1]
    if k == int(rev):
        print('pal')
    else:
        print('not pal')

pal_check(56)
#pal(56)