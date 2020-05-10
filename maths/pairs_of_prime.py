def pair(n):
    ind = 0
    lis = []
    q = 0
    for j in range(2, n+1):
        ind = prime(j)
        if ind != None:
            lis.append(ind)
    print(lis)
    for i in range(0, len(lis)):
        for j in range(i+1, len(lis)):
            if (i*j)<=n:
                print(lis[i], lis[j])

def prime(num):
    count = 0
    for i in range(2, num+1):
        if num%i == 0:
            count += 1
        if count > 2:
            break
    if count <= 1:
        return i

pair(4)
