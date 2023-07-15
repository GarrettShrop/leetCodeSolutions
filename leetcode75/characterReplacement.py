class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        c_frequency = {}
        longest_str_len = 0
        for r in range(len(s)):

            if not s[r] in c_frequency:
                c_frequency[s[r]] = 0
            c_frequency[s[r]] += 1

            # Replacements cost = cells count between left and right - highest frequency
            cells_count = r - l + 1
            if cells_count - max(c_frequency.values()) <= k:
                longest_str_len = max(longest_str_len, cells_count)
            
            else:
                c_frequency[s[l]] -= 1
                if not c_frequency[s[l]]:
                    c_frequency.pop(s[l])
                l += 1
        
        return longest_str_len
# goal is to try and find the longest substring of the same characters. so we make a dictionary named c_frequency
# we then start with a for loop for the range of the string s and use r to go through the string. we check to see
# if the character at s[r] is in our dictionary and if its its not we add it and originally set it = 0. then it
# gets incremented by 1 since we have seen 1. next we calculate the replacement cost which would be how many characters
# we need to change to get all the characters the same using the highest frequency character in out dictionary.
# if the replacement cost is less k which is given to us in the problem then we set the longest_str_len to a new max. 
# if it is more than k we move our l pointer to the left and decrease the frequency of whatever character it was on 
# because it will outside our sliding window. then if the frequency of that character hits 0 we pop it off the dictionary
# and then move l to the right by 1 and repeat until we 

# Another version i really like more but it uses get which i was not familar with
        # l = 0
        # freq = {}
        # maxlen = 0
        # for r in range(len(s)):
        #     # If a character is not in the frequency dict, this inserts it with a value of 1 (get returns 0, then we add 1).
        #     # If a character is in the dict, we simply add one.
        #     freq[s[r]] = freq.get(s[r], 0) + 1
             
        #     # The key point is that we only care about the MAXIMUM of the seen values.
        #     # Get the length of the current substring, then subtract the MAXIMUM frequency. See if this is <= K for validity.
        #     cur_len = r - l + 1
        #     if cur_len - max(freq.values()) <= k:  # if we have replaced <= K letters, record a new maxLen
        #         maxlen = max(maxlen, cur_len)
        #     else:                               # if we have replaced > K letters, then it's time to slide the window
        #         freq[s[l]] -= 1                 # decrement frequency of char at left pointer, then increment pointer
        #         l += 1
               
        # return maxlen