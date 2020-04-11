from collections import deque

open_list = ['(', '{', '[']
close_list = [')', '}', ']']
def check(mystr):
    stack = deque()
    for i in mystr:
        if i in open_list:
            stack.append(i)
        elif i in close_list:
            pos = close_list.index(i)
            if((len(stack)>0) and (open_list[pos] == stack[len(stack)-1])):
                stack.pop()
            else:
                return "unbalanced"
    if(len(stack)==0):
        return "balanced"
    else:
        return "unbalanced"
str = '([])'
print(check(str))
    
    

