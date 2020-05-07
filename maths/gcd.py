import time
def find_gcd(a,b):
    max_index = 1
    if a < b:
        for i in range(1, a+1):
            if a%i == 0 and b%i == 0:
                if i > max_index:
                    max_index = i*max_index
        return max_index
    else:
        for i in range(1, a+1):
            if a%i == 0 and b%i == 0:
                if i > max_index:
                    max_index = i*max_index
        return max_index



print(find_gcd(98, 56))
tic = time.time()
print(1000*tic)

        
                