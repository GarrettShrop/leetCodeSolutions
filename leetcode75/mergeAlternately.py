class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ''
        for i in range(min(len(word1),len(word2))):
            res += word1[i] + word2[i]
        return res + word1[i+1:] + word2[i+1:]
# for loop to run for the length of the smallest word we are given. we then alternate by
# adding word1[i] and word2[i] every loop till we get to the smallest len. then 
# we take res which is so far the combined word till the smallest len and include the rest
# of the word that is longer if it is longer if they are equal then word1[i+1:] and word2[i+1:]
# are empty and just res is returned