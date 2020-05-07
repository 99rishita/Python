def gcd(a, b):
    if b==0:
        return a
    return gcd(b, a%b)

def lcm(a, b):
    l = int(a*b/gcd(a,b))
    print(l)

lcm(24, 26)
    