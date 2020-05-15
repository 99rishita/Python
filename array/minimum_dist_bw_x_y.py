import sys


# your task is to complete this function
# function should return an integer
def minDist(arr, n, x, y):
    # Code here
    p = -1
    min_dist = sys.maxsize
    
    for i in range(0, n):
        if arr[i] == x or arr[i] == y:
            
            if p != -1 and arr[i] != arr[p]:
                min_dist = min(min_dist, i-p)
            p = i
            
    if min_dist == sys.maxsize:
        return -1
    return min_dist