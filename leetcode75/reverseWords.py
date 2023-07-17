class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        words.reverse()
        res = ' '.join(words)
        return res
# this was pretty straight forward first one i did without looking at a solution.
# i knew i had to split it on the spaces and then i needed to print it out backwards
# originally didnt understand the problem well and did s[::-1] which just reversed
# the letters and didnt keep the words. so then i looked up to remember how to split
# and also how to reverse a list and then i added that to res which had the white space
# to make it a proper sentence and not just one word all together. then we just return that string. 
