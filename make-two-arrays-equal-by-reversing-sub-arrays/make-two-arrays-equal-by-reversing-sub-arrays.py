class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        
         return collections.Counter(target) == collections.Counter(arr)
        
#         a = Counter(arr)
#         t = Counter(target)

        
#         for k, v in a.items():
            
#             if v != t[k]:
#                 return False
        
#         return True
        
        