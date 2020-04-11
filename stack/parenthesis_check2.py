from collections import deque
stack = deque()
def checkstring(mystr):
    for i in range(len(mystr)):
        if((mystr[i]=='(') or (mystr[i]=='{') or (mystr[i]=='[')):
            stack.append(i)
        if(len(stack)==0):
            return False
        elif(mystr[i] == ')'):
            x = stack.pop()
            if (x == '{' or x == '[') : 
                return False
        elif(mystr[i] == '}'):
            x = stack.pop()
            if (x == '(' or x == '[') : 
                return False
        elif(mystr[i] == ']'):
            x = stack.pop()
            if (x == '{' or x == '(') : 
                return False
    if(len(stack)==0):
        return True
    else:
        return False
String = '()}'
if(checkstring(String)):
    print('balanced')
else:
    print('Unbalanced')
        
    