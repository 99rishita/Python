val = int(input("enter size of array: "))
#print(val)
list = [1,2,3,5]
'''v = input("enter the elements: ")
for i in range(0, val):
    ele = int(input())
    list.append(ele)'''
for i in list:
    if(list[0] == 1):
        i+=1
        for j in range(1, val):
            if(i != list[j]):
                print(j)





