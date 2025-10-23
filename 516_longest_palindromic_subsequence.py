"""
Given a string s, find the longest palindromic subsequence's length in s.

A subsequence is a sequence that can be derived from another sequence by
deleting some or no elements without changing the order of the remaining elements.

Example 1:

Input: s = "bbbab"
Output: 4
Explanation: One possible longest palindromic subsequence is "bbbb".
Example 2:

Input: s = "cbbd"
Output: 2
Explanation: One possible longest palindromic subsequence is "bb".
"""


class Solution:
    # Time complexity: O(n^2)
    # Space complexity: O(n)
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp, dpPrev = [0] * n, [0] * n

        for i in range(n - 1, -1, -1):
            dp[i] = 1
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[j] = dpPrev[j - 1] + 2
                else:
                    dp[j] = max(dpPrev[j], dp[j - 1])
            dpPrev = dp[:]

        return dp[n - 1]
