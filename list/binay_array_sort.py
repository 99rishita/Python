def sort(arr, n):
    str1 = ""
    str2 = ""
    for i in arr:
        if i == 0:
            str1 = str1+str(i)
        else:
            str2 = str2+str(i)
    s = str1+str2
    print(s)
        
arr = [1,0,1,1,0,1,0,1,0,0,1]
sort(arr, len(arr))