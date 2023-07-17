class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        f = float('inf')
        s = float('inf')
        for n in nums:
            if n <= f:
                f = n
            elif n <= s:
                s = n
            elif n > s:
                return True
        return False

# was really close to solving this one without looking at solutions. 
# was just kinda brute forcing it and not accounting for going out
# of bounds. so found this solution and really makes alot of sense
# and seems really simple. we set 2 values to really high numbers 
# and then we check every number and the first if works at the beginning
# after we see if the next number is bigger than the previous if it 
# is then we can set that number to track and move to the next. 
# then if that 3rd number is bigger than s its True and by default 
# we will return False simple design but makes alot of sense. 