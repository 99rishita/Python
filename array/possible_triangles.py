def triangle(arr, n):
    a = b = 0
    count = temp = i = 0
    a = arr[n-1]
    b = arr[n-2]
    i = n-2
    count = check(a,b,c)
    while (i >= 0):
        temp = a
        a = b
        b = c
        c = arr[i-1]
        i = i-1
        count += check(a,b,c)
    print(count)


def check(a,b,c):
    count = m = 0
    m = max(a,b)
    if m == a and a+c > b and abs(a-c) < b:
        count += 1
    elif m == b and b+c > a and abs(b-c) < a:
        count += 1
    return count

arr = [6,4,9,7,8]
triangle(arr, len(arr))
    