class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_can = max(candies)
        result = []
        for i in candies:
            if i+extraCandies >= max_can:
                result.append(True)
            else:
                result.append(False)
        return result

# Method is to get the highest number of candies a kid has then also make a empty array to store True
# and False. then we just iterate through the students and compare there current candy amount 
# with the extra candies they could recieve and see if that would give them the most candies. 
# if it does then we append True to our result array and if its not the case we append False. 
# i was originally thinking of using a dictionary to store the max but the solution i looked at used 
# arrays and this section of 75 is array and strings so makes sense. will come back to this problem 
# and try new ways soon. 