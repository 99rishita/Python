def insertion_sorting(arr):
    n = len(arr)
    for i in range(1, n):
        current_ele = arr[i]
        j = i
        while(j>0 and current_ele < arr[j-1]):
            arr[j] = arr[j-1]
            j -= 1
        arr[j] = current_ele

    print(arr)

arr = [30,10,50,20,60,40]
insertion_sorting(arr) 