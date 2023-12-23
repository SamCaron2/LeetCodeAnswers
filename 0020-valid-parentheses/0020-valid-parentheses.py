class Solution(object):
    def isValid(self, s):
        stack = [] #Create an empty stack
        
        for i in s:
            if i == "(" or i == "[" or i == "{":
                stack.append(i) #if index i is any of the three open brackets append to created stack
                
            elif(len(stack)): #if it is closing brackets check to see if len > 0
                
                topOfStack = stack.pop() #get the char at the top of the stack
                
                #if the top of the stack does not match up with index i return false
                if topOfStack == "(" and i != ")":
                    return False
                elif topOfStack == "[" and i != "]": 
                    return False
                elif topOfStack == "{" and i != "}":
                    return False
                
           # If both conditions fail return false    
            else:
                return False
            
        #if there are any remaining characters in the stack return false
        if(len(stack)):
            return False
        else:
            return True
            
                
            
            