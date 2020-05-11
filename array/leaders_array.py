def leaders(arr, n):
    for l in range(0, n):
        r = n-1
        while(arr[l] >= arr[r]):
            if l == r:
                break
            r -= 1
        if r == l:
            print(arr[l])

arr = [16,17,4,3,5,2]
#arr = [7,4,5,7,3]
#arr = [1,2,3,4,0]
leaders(arr, len(arr))