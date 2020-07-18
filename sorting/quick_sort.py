def quick_sorting(arr, low, high):
    if low < high:
        pi_index = partition(arr, low, high)

        quick_sorting(arr, low, pi_index-1)
        quick_sorting(arr, pi_index+1, high)
        

def partition(arr, low, high):
    pivot = arr[high]
    i = low-1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    i += 1
    arr[i], arr[high] = arr[high], arr[i]
    return i

arr = [30,10,50,20,60,40]
quick_sorting(arr, 0, len(arr)-1)
print(arr)