"""
Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.

Example 1:

Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
Example 2:

Input: arr = [1,2]
Output: false
Example 3:

Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true
"""

from typing import List


class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occurence_count = {}

        # Count occurrences of each number
        for n in arr:
            occurence_count[n] = occurence_count.get(n, 0) + 1

        seen_counts = set()
        # Check for unique occurrence counts
        for count in occurence_count.values():
            if count in seen_counts:
                return False
            seen_counts.add(count)

        return True
