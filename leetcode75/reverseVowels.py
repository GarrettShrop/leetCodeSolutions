class Solution:
    def reverseVowels(self, word: str) -> str:
        start = 0
        end = len(word)- 1
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        s = [word[i] for i in range(len(word))]
        while start < end:
            if s[start] in vowels:
                while start < end and s[end] not in vowels:
                    end -= 1
                temp = s[start]
                s[start] = s[end]
                s[end] = temp
                end -= 1
            start += 1
        res = ""

        for i in s:
            res += i
        return res

# 2 pointer problem. so we set start to 0 and end to the len of word - 1 to get the last value. 
# we make a list of the vowels provided. we turn the word into a list s. then we start a while loop
# that checks to see if the start pointer is less than the end pointer. then if s[start] is a vowel
# we need to see if s[end] is also a vowel if end isnt a vowel then we subtract the pointer by 1
# until we find a vowel while end is greater than start. once we find a vowel at s[end] we make a 
# temp value and set it to s[start] then set the character at start equal to the character at end. 
# we then set end to temp which is what start was pointing at. after that we decrement end and increment
# start. we make a res empty string and add the reversed string into res at the end and then return res.
# looked this up as well but think i have a good understanding