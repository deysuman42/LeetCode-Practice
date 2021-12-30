class Solution:
    def numberOfMatches(self, n: int) -> int:
        
        t = 0
        while n > 1:
            if n % 2 == 0:
                matches = advance = n // 2
               
            else:
                matches = (n - 1) // 2
                advance = n - matches
            
            print(matches, advance)
            t += matches
            n = advance
            print(t)
        
        return t
                
        