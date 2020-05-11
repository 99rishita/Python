def lead(arr, n):
    max_ele = arr[n-1]
    print(max_ele)
    for i in range(n-2, -1, -1):
        if max_ele <= arr[i]:
            print(arr[i])
            max_ele = arr[i]
arr = [16, 17, 4, 3, 5, 2]
#arr = [7,4,5,7,3]
lead(arr, len(arr))
