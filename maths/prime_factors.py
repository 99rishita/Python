import math
def prime_fact(n):
    print(n, end=" ")
    print(1, end=" ")
    while n%2 == 0:
        print(2, end=" ")
        n = int(n/2)
    for i in range(3, int(math.sqrt(n))+1, 2):
        while n%i == 0:
            print(i, end=" ")
            n = int(n/i)
    if n > 2:
        print(int(n))

prime_fact(35)
    
