def array_gcd(x, y):
    if y == 0:
        return x
    return array_gcd(y, x%y)

arr = [2, 4, 6, 8, 16] 
n1 = arr[0]
n2 = arr[1]
gcd = array_gcd(n1, n2)

for i in range(2, len(arr)):
    gcd = array_gcd(gcd, arr[i])

print(gcd)      

            