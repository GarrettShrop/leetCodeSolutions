class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        frequency1 = {}
        frequency2 = {}

        for letter in word1:
            frequency1[letter] = frequency1.get(letter, 0) + 1

        for letter in word2:
            frequency2[letter] = frequency2.get(letter, 0) + 1

        if set(frequency1.keys()) != set(frequency2.keys()):
            return False

        if sorted(frequency1.values()) != sorted(frequency2.values()):
            return False

        return True

"""
This was a medium problem and with talking to Claude i was able to get the problem going pretty well on my own. I checked the len
of each word since they needed to be the same. Then i created the two dictionaries and got the letters for the keys and the number
of times we see those letters as the values. Next i was able to set the keys to sets and compare them for differences since we need the same
characters in each word. Then claude suggested the sort on the values which makes sense so we can just see if the frequencies are the same
regardless of the characters.
"""