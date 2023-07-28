class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # base case - not same length
        if (len(s) != len(t)):
            return False
        # base case - empty set (assuming they're same length from case above)
        if len(s) == 0 or len(t) == 0:
            return True

        # create a list size 26 (index 0 represents 'a' and index 25 represents 'z')
        letters = [0]*26

        # iterate over the length of s & t (assuming they're same length)
        # and increase each letter s has in letters and decrease for t
        for i in range(len(s)):
            letters[ord(s[i]) - ord('a')] += 1
            letters[ord(t[i]) - ord('a')] -= 1

        # iterate over letters and to see if it contains all zeros
        for i in range(len(letters)):
            # if it is not a 0 then the letters do not match up
            if letters[i] != 0:
                return False

        # same number of letters, therefore true
        return True