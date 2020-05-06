import time

def jump_num(num):
    flag = 0
    for i in range(0, num):
        if i <= 10 and i >= 0:
            print(i, end=" ")
        else:
            f = check_con(i)
            if f == 1:
                print(i, end=" ")

def check_con(n):
    s = str(n)
    for i in range(len(s)-1, 0, -1):
        r = int(s[i])-int(s[i-1])
        if abs(r) == 1:
            continue
        else:
            return 0
    return 1
            
jump_num(50)
tic = time.time()
print(round(1000*tic))

