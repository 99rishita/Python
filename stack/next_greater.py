def greater(arr):
    for i in range(0,len(arr)):
        next=-1
        for j in range(i+1, len(arr)):
            if(arr[j]>arr[i]):
                next=arr[j]
                break
        print(next)
arr=[4,3,2,1]
greater(arr)

