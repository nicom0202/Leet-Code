class Solution:
    def isPalindrome(self, s: str) -> bool:
        # base case - empty string
        if len(s) == 0:
            return True

        # base case - one letter string
        if len(s) == 1:
            return True

        # two pointer technique 
        front = 0
        back = len(s) - 1
        while front < back:
            # if not alphanumeric, skip
            if not s[front].isalnum():
                front += 1
                continue
            
            # if not alphanumeric, skip
            if not s[back].isalnum():
                back -= 1
                continue
            
            # change character to lowercase, then check if they are the same
            if s[front].lower() != s[back].lower():
                return False
            front += 1
            back -= 1

        return True