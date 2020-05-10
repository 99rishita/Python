def remove_duplicate(n, arr):
    #Code here
    for i in range(n-1,0,-1):
        if arr[i] == arr[i-1]:
            arr.remove(arr[i])
        else:
            continue
    return len(arr)
