"""
Given a string s and an integer k, return true if s is a k-palindrome.

A string is k-palindrome if it can be transformed into a palindrome by removing at most k characters from it.

Example 1:

Input: s = "abcdeca", k = 2
Output: true
Explanation: Remove 'b' and 'e' characters.
Example 2:

Input: s = "abbababa", k = 1
Output: true
"""

from functools import lru_cache


class Solution:
    # Time complexity: O(n^2)
    # Space complexity: O(n^2)
    def isValidPalindrome(self, s: str, k: int) -> bool:
        @lru_cache(None)
        def min_deletions(left: int, right: int) -> int:
            # Base case: single char or empty string
            if left >= right:
                return 0

            if s[left] == s[right]:
                return min_deletions(left + 1, right - 1)

            # If mismatch → need one deletion (either left or right)
            return 1 + min(
                min_deletions(left + 1, right), min_deletions(left, right - 1)
            )

        return min_deletions(0, len(s) - 1) <= k
