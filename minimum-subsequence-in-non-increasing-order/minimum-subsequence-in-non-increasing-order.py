class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        
        heap = []
        out = []
        s = sum(nums)
        sub_sum = 0
        
        for i in nums:
            heapq.heappush(heap, (-i))
        
        
        while True:
            
            x = heapq.heappop(heap)
            sub_sum += abs(x)
            s -= abs(x)
            
            if s >= sub_sum:
                out.append(abs(x))
            else:
                out.append(abs(x))
                break;
        
        return out
            
        
#         nums.sort()
#         s = sum(nums)
#         sub_sum = 0
#         ind = 0
        
#         for i in range(len(nums)-1, -1, -1):
            
#             sub_sum += nums[i]
#             s -= nums[i]
            
#             if s >= sub_sum:
                
#                 continue
            
#             else:
                
#                 ind = i
#                 break;
           
        
#         return nums[ind:][::-1]
        