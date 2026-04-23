"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true

Example 2:

Input: s = "rat", t = "car"
Output: false
"""

class Solution:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        if s == t:
            return True

        count = [0] * 26  # assuming only lowercase letters

        for char_s, char_t in zip(s, t):
            count[ord(char_s) - ord('a')] += 1
            count[ord(char_t) - ord('a')] -= 1

        return all(c == 0 for c in count)