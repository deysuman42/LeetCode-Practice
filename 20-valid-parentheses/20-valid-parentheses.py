class Solution:
    def isValid(self, s: str) -> bool:
        
        closetoopen = {')' : '(', '}' : '{', ']' : '['}
        stack = []
        
        for i in s:
            
            if i in closetoopen:
                if (stack) and stack[-1] == closetoopen[i]:
                    stack.pop()
                    continue
                else:
                    return False
                
            else:
                stack.append(i)
        
        return not stack
        
        
       