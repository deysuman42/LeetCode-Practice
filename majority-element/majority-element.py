class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
      
    
        count = 0
        candidate = None
    

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)
            # print(candidate, count)

        
        return candidate

    
    
#         a = [(-v, k) for k, v in collections.Counter(nums).items() if v > (len(nums) // 2)]
        
#         return heapq.heappop(a)[1]
        