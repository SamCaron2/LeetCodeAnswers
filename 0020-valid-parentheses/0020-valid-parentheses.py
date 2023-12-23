class Solution(object):
    def isValid(self, s):
        stack = []
        
        for i in s:
            if i == "(" or i == "[" or i == "{":
                stack.append(i)
            elif(len(stack)):
                topOfStack = stack.pop()
                if topOfStack == "(" and i != ")":
                    return False
                elif topOfStack == "[" and i != "]":
                    return False
                elif topOfStack == "{" and i != "}":
                    return False
                
            else:
                return False
        if(len(stack)):
            return False
        else:
            return True
            
                
            
            