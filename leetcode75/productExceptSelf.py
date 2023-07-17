class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        sol = [1] * length
        pre = 1
        post = 1
        for i in range(length):
            sol[i] *= pre
            pre = pre * nums[i]
            sol[length - i - 1] *= post
            post = post * nums[length - i - 1]
        return sol

# needed some help on this on originally had 2 for loops going and getting the product
# but it wasnt giving the right solutions. so i looked a single for loop function 
# solution so it runs 1 for loop and we have a pre and post pointer. the pre multiplys
# all the numbers except for the current i and post gets the product of all the numbers
# after the i and then that makes up out sol list which we return at the end of the nums list.
# has some trouble on this one conceptually will be revisting often i think. 