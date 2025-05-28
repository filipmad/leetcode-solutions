# LeetCode 28/05/2025
# Longest Substring Without Repeating Characters

#Given a string s, find the length of the longest substring without duplicate characters.
class Solution(object):
    def lengthOfLongestSubstring(self, s):

        # Keep the length of s for calculation
        max_length = len(s)

        # Keep track longest string
        longest_string_length = 0

        # Go through each substring in s
        for i in range(max_length):
            substring = ""
            
            # Generate each substring until you reach a repeated letter
            # or reach the end
            j = i
            while (j < max_length and s[j] not in substring):
                substring = substring + s[j]
                j += 1    

            # Update longest_string if a longer substring has been found
            longest_string_length = max(len(substring), longest_string_length)


        return longest_string_length
        """
        :type s: str
        :rtype: int
        """
        