def greater(arr):
    for i in range(0,len(arr)):
        for j in range(i+1, len(arr)):
            next=-1
            if(arr[j]>arr[i]):
                next=arr[j]
                print(arr[j])
                break
            else:
                print(next) 
arr=[1,3,2,4]

