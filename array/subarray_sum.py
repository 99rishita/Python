def subarray(arr, len, sum):
    
    for i in range(len):
        s = 0
        for j in range(i, len):
            s = s+arr[j]
            if(sum==s):
                print("sum between indexes")
                print("%d and %d"%(i ,j))
                #print(i , j)
                return 1
    print("no subarray found")
    return 0
array = [9,2,3,0,3,1,3,9]
len = len(array)
sum = 8
subarray(array, len, sum)
