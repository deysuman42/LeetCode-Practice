class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        
        largest = max(nums)
        index = -1
        for i in range(len(nums)):
            if largest == nums[i]:
                index = i
        print(index)
        for i in range(len(nums)):
            if (largest < nums[i] * 2) and (i != index):
                print(i)
                return -1
        return index