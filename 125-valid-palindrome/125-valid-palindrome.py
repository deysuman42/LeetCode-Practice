class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        print(s[0].isalnum())
        left = 0
        right = len(s) - 1
        
        while left < right:
            
            if not s[left].lower().isalnum():
                left += 1
            elif not s[right].lower().isalnum():
                right -= 1
            elif s[left].lower() == s[right].lower():
                left += 1
                right -= 1
            else:
                return False
        return True
            
            
        