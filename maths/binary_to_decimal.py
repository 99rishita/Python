def convert(n):
    rem = sum = i = 0
    while(n > 0):
        rem = n % 10
        sum = sum + rem*(2 ** i)
        n = int(n/10)
        i += 1
    print(sum)

convert(10001000)