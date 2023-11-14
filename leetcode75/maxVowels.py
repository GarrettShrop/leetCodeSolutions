class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        lib = {'a', 'e', 'i', 'o', 'u'}
        max_vowel = 0
        curr_vowel = 0
        for i in range(k):
            if s[i] in lib:
                curr_vowel += 1
        max_vowel = curr_vowel
        for i in range(k, len(s)):
            if s[i - k] in lib:
                curr_vowel -= 1
            if s[i] in lib:
                curr_vowel += 1
            max_vowel = max(curr_vowel, max_vowel)
        return max_vowel

# Time Complexity: O(n)
# Space Complexity: O(1)
# so here we are using a sliding window. we are adding the first k elements and storing it in curr_vowel.
# then we are iterating through the rest of the array and adding the next element and removing the first element
# from the sum. then we are comparing the sum to the answer and storing the max value. then we are returning the
# answer divided by k. i think this is a good solution. i think i need to practice more with sliding windows.
