class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
         
        out = []
        nums.sort()
        
        print(nums)
        
        left_static = 0
#         left_floating = left_static + 1
#         right_floating = len(nums) - 1
        
        while left_static < (len(nums) - 2):
            
            left_floating = left_static + 1
            right_floating = len(nums) - 1
            
            while (left_floating < right_floating):
                
            
                if (nums[left_static] + nums[left_floating] + nums[right_floating]) == 0:
                    if [nums[left_static],nums[left_floating],nums[right_floating]] not in out:
                        out.append([nums[left_static],nums[left_floating],nums[right_floating]] )
                    left_floating += 1
                    right_floating -= 1
                    
                elif (nums[left_static] + nums[left_floating] + nums[right_floating]) < 0:
                    left_floating += 1
                
                elif (nums[left_static] + nums[left_floating] + nums[right_floating]) > 0:
                    right_floating -= 1
            
            left_static += 1
        
        return out

            
        