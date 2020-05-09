import math
def generate_factors(n):
    lower_bound_check = int(math.sqrt(n))  # determine lowest bound divisor range [16 = 4]
    factors = set()  # store factors
    for divisors in range(1, lower_bound_check + 1):  # loop [1 .. 4]
        if n % divisors == 0:
            factors.add(divisors)  # lower bound divisor is found 16 [ 1, 2, 4]
            factors.add(n // divisors)  # get upper divisor from lower [ 16 / 1 = 16, 16 / 2 = 8, 16 / 4 = 4]
    return factors  # [1, 2, 4, 8 16]


print(generate_factors(35))