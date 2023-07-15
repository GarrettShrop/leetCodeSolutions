class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if(str1 + str2 != str2 + str1):
            return ""
        
        return  str1[:math.gcd(len(str1), len(str2))]

# if str1 + str2 are not equal to str2 + str1 then there is no commond denominator so return empty
# otherwise we know there is some gcd so we can use the gcd function that we get from math
# and take the len of str1 and str2 and set that to a substring of str1 and return that so it just gets
# the gcd of the 2 strings
