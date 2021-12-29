class Solution:
    def specialArray(self, nums: List[int]) -> int:
        
        nums.sort()
        for i in range(1, len(nums) + 1):
            startIndex = bisect.bisect_left(nums, i)
            print(startIndex)
            if len(nums) - startIndex == i:
                return i
        return -1