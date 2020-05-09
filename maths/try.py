def factors(n):
    factors = []
    for i in range(1, (n//2)+1):
        if n % i == 0:
            factors.append (i)
    factors.append(n)

    return factors

print(factors(20))