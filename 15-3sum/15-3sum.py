class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        
        nums.sort()
        res = []

        for j in range(0, len(nums)-2):
            if (j > 0) and (nums[j] == nums[j-1]):
                continue
            left = j + 1
            right = len(nums) - 1


            while (left < right):

                three_sum = nums[j] + nums[left] + nums[right]
                if three_sum == 0:
                    res.append([nums[j], nums[left], nums[right]])
                    left += 1
                    while (left < right) and (nums[left] == nums[left - 1]):
                        left += 1
                elif three_sum > 0:
                    right -= 1
                else:
                    left += 1
        return res
         
#         res = []
#         nums.sort()
        
#         for i, a in enumerate(nums):
#             if i > 0 and a == nums[i - 1]:
#                 continue
            
#             l, r = i + 1, len(nums) - 1
#             while l < r:
#                 threeSum = a + nums[l] + nums[r]
#                 if threeSum > 0:
#                     r -= 1
#                 elif threeSum < 0:
#                     l += 1
#                 else:
#                     res.append([a, nums[l], nums[r]])
#                     l += 1
#                     while nums[l] == nums[l - 1] and l < r:
#                         l += 1
#         return res
            
        