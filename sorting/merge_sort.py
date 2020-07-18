def merge_sorting(arr):
    n = len(arr)
    mid = 0
    if n>1:
        mid = n//2
        l = arr[:mid]
        r = arr[mid:]
        merge_sorting(l) # sort first half
        merge_sorting(r) # sort second half

        i = j = k = 0

        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                arr[k] = l[i]
                i += 1
                k += 1
            else:
                arr[k] = r[j]
                j += 1
                k += 1
        
        #to check if any of the element is left
        while i < len(l):
            arr[k] = l[i]
            i += 1
            k += 1
        
        while j < len(r):
            arr[k] = r[j]
            j += 1
            k += 1

'''def printList(arr): 
    for i in range(len(arr)):         
        print(arr[i], end =" ") 
    print() '''

arr = [30,10,50,20,60,40]
merge_sorting(arr)
print("Sorted array is: ", end ="\n") 
#printList(arr)
print(arr) 