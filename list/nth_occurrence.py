def list(newlist, word, n):
    global count
    for i in range(0, len(newlist)):
        if(newlist[i]==word):
            count+=1
            if(count==n):
                del(newlist[i])
                return True
    return False
count=0
newlist = [1,2,2,5,2]
word = 2
n = 3
if((list(newlist, word, n))==True):
    print(newlist)
else:
    print("item not found")



