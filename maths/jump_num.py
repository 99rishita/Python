import time
from collections import deque


def bfs(x, num):
    q = deque()
    q.append(num)

    while(len(q)):
        num = q.pop()
        
        if num <= x:
            print(num, end=" ")
            last_digit = num%10

            if last_digit == 0:
                q.append((num*10)+(last_digit+1))

            elif last_digit == 9:
                q.append((num*10)+(last_digit-1))
            else:
                q.append((num*10)+(last_digit-1))
                q.append((num*10)+(last_digit+1))

def search(x):
    print(0, end=" ")
    for i in range(1,10):
        bfs(x, i)

x = 40
search(x)
tic = time.time()
print(1000*tic)

