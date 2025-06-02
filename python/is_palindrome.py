# 02/06/2025 Leetcode
# Given an integer x, return true if x is a palindrome, and false otherwise.
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        xString = str(x)

        l = 0
        r = len(xString) - 1
        final_length = 0

        

        # Meet in the middle
        while (l <= r):
            if (xString[l] != xString[r]):
                return False
            
            # Adjust Variables
            final_length += 1
            l += 1
            r -= 1
        
        return True
