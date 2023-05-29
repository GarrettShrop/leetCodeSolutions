from ast import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sumLeft = 0
        sumRight = sum(nums)
        for i in range(len(nums)):
            sumRight -= nums[i]
            if sumLeft == sumRight:
                return i
            sumLeft += nums[i]
        return -1