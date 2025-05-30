class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        if n == 0:
            return ""
        
        start, maxLen = 0, 1

        # Traverse the input string
        for i in range(n):
            
            # THIS RUNS TWO TIMES 
            # for both odd and even length
            # palindromes. j = 0 means odd
            # and j = 1 means even length
            for j in range(2):
                low, high = i, i + j

                # Expand substring while it is a palindrome
                # and in bounds
                while low >= 0 and high < n and s[low] == s[high]:
                    currLen = high - low + 1
                    if currLen > maxLen:
                        start = low
                        maxLen = currLen
                    low -= 1
                    high += 1
        
        return s[start:start + maxLen]
       