import math
import time
def gcd_find(a,b):
    if b == 0:
        return a
    else:
        return gcd_find(b, a%b)

'''a = 60
b = 48'''

print(gcd_find(60,48))
tic = time.time()
print(1000*tic)
print(math.gcd(98,56)) 

    
    