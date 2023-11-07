class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        maxArea = 0

        while left < right:
            currentArea = min(height[left], height[right]) * (right - left)
            maxArea = max(maxArea, currentArea)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return maxArea

# Time Complexity: O(n)
# Space Complexity: O(1)
# this solution is from the solutions tab. I was thinking about how we would compare the heights. 
# i didnt think about how ive been learning using 2 pointers to sort but it coould be used here. 