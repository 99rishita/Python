import time
def sieve(n):
    for j in range(2, n+1):
        prime_check(j)

def prime_check(num):
    count = 0
    for i in range(2, num+1):
        if num%i == 0:
            count += 1
        if count > 2:
            break
    if count <= 1:
        print(i, end=" ")

sieve(20)
tic = time.time()
print(1000*tic)
