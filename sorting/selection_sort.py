def selection_sort(arr):
    n = len(arr)
    min_index = 0
    for i in range(0, n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    print(arr)

arr = [30,10,50,20,60,40]
selection_sort(arr) 
