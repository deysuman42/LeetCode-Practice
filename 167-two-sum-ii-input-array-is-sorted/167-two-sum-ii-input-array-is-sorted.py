class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        
        
        # numbers.sort()
        res = []

        left = 0
        right = len(numbers) - 1

        while (left < right):
            
            two_sum = numbers[left] + numbers[right]
            if two_sum == target:
                # res.append(left + 1, right + 1)
                return [left + 1, right + 1]
                left += 1
                
                while (left < right) and (nums[left] == nums[left - 1]):
                    left += 1

            elif two_sum > target:
                right -= 1
            else:
                left += 1
        return res
        
#         left = 0
#         right = len(numbers) - 1
        
#         while left < right:
            
#             if (numbers[left] + numbers[right]) == target:
#                 return [left+1, right+1]
#             elif (numbers[left] + numbers[right]) > target:
#                 right -= 1
#             elif (numbers[left] + numbers[right]) < target:
#                 left += 1
#         return [-1, -1]
        
        
        