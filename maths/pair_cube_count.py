import math
def pair_cube(n):
    count = 0
    for i in range(1, int(math.pow(n, 1/3))+1):
            diff = n - i**3
            check_diff = int(math.pow(diff, 1/3))
            if check_diff**3 == diff:
                count += 1
    return count

print(pair_cube(27))

 
