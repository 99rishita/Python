def rotate(arr, n, d):
    arr = arr[d:len(arr)] + arr[0:d]
    print(arr)

#arr = [1,2,3,4,5]
arr = [2,4,6,8,10,12,14,16,18,20]
rotate(arr, len(arr), 3)
           
