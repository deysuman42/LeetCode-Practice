class Solution:
    def checkString(self, s: str) -> bool:
        
        return 'ba' not in s
        
#         pos_a = -1
#         pos_b = len(s)
        
#         for i in range(0, len(s)):
#             if s[i] == 'a':
               
#                 pos_a = i
               
#             else:
#                 if i < pos_b:
#                     pos_b = i
       
#         return pos_a < pos_b
        