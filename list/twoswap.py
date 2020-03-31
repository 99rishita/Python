def swaplist(newlist, pos1, pos2):
    newlist[pos1], newlist[pos2] = newlist[pos2], newlist[pos1]
    return newlist
newlist = [1,2,3,4,5]
print(swaplist(newlist,1,3))