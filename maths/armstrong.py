def armstrong(n):
    sum = 0
    while(n>0):
        rem = n%10
        sum = rem ** 3 + sum
        n = int(n/10)
    return sum

print(armstrong(371))