from sys import maxsize
def largest_sum(arr, n):
    
    sum_largest = -maxsize-1
    sum=0
    for i in range(0, n):
        sum = sum+arr[i]
        if(sum>sum_largest):
            sum_largest=sum
        if(sum<0):
            sum=0
    print(sum_largest)
array = [-1, -2, -3, -4]
len = len(array)
largest_sum(array, len)