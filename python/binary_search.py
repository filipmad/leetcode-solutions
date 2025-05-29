# LeetCode 29/05/2025

# Binary Search

# Given an array of integers nums which is sorted in ascending order, and an integer target, 
# write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        r = len(nums)
        l = 0
        while (l < r):
            
            # Set k as the midpoint between r and l
            k  = l + (r - l) // 2

            # Termination: Target Found at k
            if (nums[k] == target):
                return k
            
            # Undershot the target: Prune the first half of the list
            if (nums[k] > target):
                r = k
            
            # Overshot the target: Prune the second half of list            
            else:
                l = k + 1
        
        return -1
        