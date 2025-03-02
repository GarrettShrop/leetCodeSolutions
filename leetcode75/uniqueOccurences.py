class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        frequency = {}

        for num in arr:
            frequency[num] = frequency.get(num, 0) + 1

        uniqueVals = set(frequency.values())

        if len(uniqueVals) == len(frequency):
            return True
        
        return False

# This was a good problem. I used Claude but i didn't give me any code but instead ask my questions to help me work through the answer.
# It also provided some knowledge about using a set to get the unique frequencies. I like the fact of creating the dictionary and storing the num
# and the number of times it occurs with the for loop. Then we pull the unique values and put them in a set. Then we can compare the len of the set
# and the dictionary and if its equal then we can return True and if not we return False. 