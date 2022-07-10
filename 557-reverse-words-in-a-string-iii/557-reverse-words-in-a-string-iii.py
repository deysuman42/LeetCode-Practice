class Solution:
    def reverseWords(self, s: str) -> str:
        
        
        res = ""
        s += " "
        l = 0
        r = 0
        
        while r < len(s):
            if s[r] != " ":
                r += 1
            elif s[r] == " ":
                res += s[l:r+1][::-1]
                r += 1
                l = r
        return res[1:]
    
        
        
#         res = ' '

#         left = 0
#         right = 0
        
#         print(s[right])
        
#         while (s[right] != ' ') and (right < len(s)):
#             right += 1
#         res += s[left:right+1][::-1]
#         print(left, right)
#         right += 1
#         left = right
#         print(res)
        
# #         s = s.split(' ')
        
# #         for i, a in enumerate(s):
# #             s[i] = s[i][::-1]
            
# #         return " ".join(s)
        
    