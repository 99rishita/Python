def tri(arr, n):
    arr.sort()
    count = 0
    for i in range(n-1, 0, -1):
        l = 0  
        r = i-1
        while(l<r):
            if arr[l] + arr[r] > arr[i]:
                count += r-l
                r -= 1
            else:
                l += 1
    print(count)

arr = [6, 4, 9, 7, 8]
tri(arr, len(arr))
    