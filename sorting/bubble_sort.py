def bubble_sort(arr):
    n = len(arr)
    for i in range(0, n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    print(arr)
            
arr = [30,10,50,20,60,40]
bubble_sort(arr)