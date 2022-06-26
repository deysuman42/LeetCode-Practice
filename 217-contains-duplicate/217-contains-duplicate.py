from collections import defaultdict
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        
#         h = defaultdict(int)
        
#         for i in nums:
#             if i not in h:
#                 h[i] += 1
#             else:
#                 return True
#         return False

        hashset = set()
        
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False