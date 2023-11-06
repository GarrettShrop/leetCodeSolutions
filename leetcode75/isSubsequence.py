class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_index = t_index = 0

        while s_index < len(s) and t_index < len(t):
            if s[s_index] == t[t_index]:
                s_index += 1
            t_index += 1
        
        return s_index == len(s)

# so originally i wanted to use a dictionary and store the count of each letter
# for string s and string t. then i would compare both dictionaries and see if they match
# i was getting some errors with this method so i looked at the solutions and this made sense
# to me. we have 2 pointers one for each string and we check if the letter at the first pointer
# is equal to the letter at the second pointer. if it is then we increment both pointers and
# continue. if not then we just increment the second pointer. if the first pointer reaches the
# end of the string then we know that all the letters in s are in t and we return True. if the
# second pointer reaches the end of the string then we know that all the letters in s are not
# in t and we return False.