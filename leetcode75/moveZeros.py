class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0 and nums[slow] == 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]

            if nums[slow] != 0:
                slow += 1

# So this makes sense i was originally thinking we needed to sort
# the list but that isnt the case. its a simpler 2 pointer problem. 
# so we have fast and slow. so we iterate through the loop with fast
# and if fast is not zero and slow which would be 0 at the start
# we switch the values. if fast is 0 and slow is a number then we just 
# increment slow and and keep going till we get slow on a 0 and fast on
# a non zero number. then after the switching all the numbers shoule be 
# ahead of the zeros. im having a bit of a hard time concentrating on
# the plane so im finding myself just going to the answer sooner than id 
# like so ill end my leetcode work for tonight. 