class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        if len(nums) == 0:
            return 0
        else:
            left = 0
            right = len(nums) - 1
            count = 0
            while left < right:
                if (nums[left] + nums[right]) == k:
                    count += 1
                    left += 1
                    right -= 1
                elif (nums[left] + nums[right]) < k:
                    left += 1
                else:
                    right -= 1
        return count
#this was my first attempt without looking at solutions or any help and i passed the run test cases but
# only 12/51 test cases. after this i looked at chatgpt and it recommended having a variable for the sum
# so ill try that now.
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        if len(nums) == 0:
            return 0
        else:
            nums.sort()
            left = 0
            right = len(nums) - 1
            count = 0
            while left < right:
                currSum = nums[left] + nums[right]
                if currSum == k:
                    count += 1
                    left += 1
                    right -= 1
                elif currSum < k:
                    left += 1
                else:
                    right -= 1
            return count
# here is the code that chatgpt recommended. i passed 51/51 test cases. i think i was on the right track
# but i wasnt sure how to implement it. i think i need to practice more with 2 pointers. i am happy that 
# for the first time recently i was able to have a passable run case with just thinking even if its just
#  a simpler problem. the only difference im seeing is that im sorting the array first. i think it makes
# it easier to compare the sum to the target. 
