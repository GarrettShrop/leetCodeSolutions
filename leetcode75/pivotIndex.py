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

# Time Complexity: O(n)
# Space Complexity: O(1)
# So for this problem we set suumLeft to 0 and then we put sumRight to the total sum of the array. 
# Then we go through the array and subtract the current element from sumRight. Then we compare sumLeft
# to sumRight and if they are equal then we return the index. If not then we add the current element
# to sumLeft and continue. If we go through the whole array and dont find the pivot index then we
# return -1.