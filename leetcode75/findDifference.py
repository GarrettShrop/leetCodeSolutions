class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1 = set(nums1)
        set2 = set(nums2)

        result = [list(set1 - set2), list(set2 - set1)]

        return result

"""
I really liked how simple this problem was. It was just turning the two lists each into a set and then we check the difference both ways
I made the mistake of thinking i needed to remove the [ ] around the two lists and learned that if i don't have them then i create a tuple instead
of a list with lists in it. So after fixing that i got the right answer.
"""