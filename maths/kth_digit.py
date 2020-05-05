def digit_k(a, b, k):
    num = 0
    num = a ** b
    #print(num)
    num = str(num)
    result = int(num[-k])
    print(result)
    


digit_k(7,6,3)

