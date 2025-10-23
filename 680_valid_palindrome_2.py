"""
Given a string s, return true if the s can be palindrome after deleting at most one character from it.

Example 1:

Input: s = "aba"
Output: true
Example 2:

Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.
Example 3:

Input: s = "abc"
Output: false
"""


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome(left: int, right: int) -> bool:
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1

            return True

        left, right = 0, len(s) - 1

        while left < right:
            if s[left] != s[right]:
                # Try skipping either the left or right character
                return is_palindrome(left + 1, right) or is_palindrome(left, right - 1)
            left += 1
            right -= 1
        return True
