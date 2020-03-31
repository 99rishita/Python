def triplets(arr, n):
    sum=0
    count=0
    for i in range(n):
        for j in range(i+1, n):
            sum = arr[i]+arr[j]
            for k in range(n):
                if(sum==arr[k]):
                    count+=1
    print(count)
array = [1, 1, 1, 2, 2]
len = len(array)
triplets(array, len)