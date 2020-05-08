import math
def prime_fact(n):
    max_ind = 0
    #print(n, end=" ")
    #print(1, end=" ")
    while n%2 == 0:
        #print(2, end=" ")
        n = int(n/2)
    for i in range(3, int(math.sqrt(n))+1, 2):
        while n%i == 0:
            #print(i, end=" ")
            n = int(n/i)
            if i > max_ind:
                max_ind = i
                #print(max_ind)
    if n > 2:
        if n > max_ind:
            print(n)
        else:
            print(max_ind)

prime_fact(15)
