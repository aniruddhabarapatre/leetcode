"""
You are given a string s consisting of lowercase English letters.
A duplicate removal consists of choosing two adjacent and equal letters and removing them.

We repeatedly make duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made. It can be proven that the answer is unique.

Example 1:

Input: s = "abbaca"
Output: "ca"
Explanation:
For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal,
and this is the only possible move.  The result of this move is that the string is "aaca",
of which only "aa" is possible, so the final string is "ca".
"""


class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def removeDuplicates(self, s: str) -> str:
        stack = []

        for ch in s:
            if stack and stack[-1] == ch:
                stack.pop()
            else:
                stack.append(ch)

        return "".join(stack)


# Variant: In-place modification
class Solution2:
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def removeDuplicates(self, s: str) -> str:
        s_list = list(s)
        ix = 0

        for i in range(len(s_list)):
            if ix > 0 and s_list[ix - 1] == s_list[i]:
                ix -= 1
            else:
                s_list[ix] = s_list[i]
                ix += 1

        return "".join(s_list[:ix])
