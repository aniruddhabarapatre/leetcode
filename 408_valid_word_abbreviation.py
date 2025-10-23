"""
A string can be abbreviated by replacing any number of non-adjacent, non-empty substrings with their lengths.
The lengths should not have leading zeros.

For example, a string such as "substitution" could be abbreviated as (but not limited to):

    "s10n" ("s ubstitutio n")
    "sub4u4" ("sub stit u tion")
    "12" ("substitution")
    "su3i1u2on" ("su bst i t u ti on")
    "substitution" (no substrings replaced)

The following are not valid abbreviations:

    "s55n" ("s ubsti tutio n", the replaced substrings are adjacent)
    "s010n" (has leading zeros)
    "s0ubstitution" (replaces an empty substring)

Given a string word and an abbreviation abbr, return whether the string matches the given abbreviation.

A substring is a contiguous non-empty sequence of characters within a string.


Example 1:

Input: word = "internationalization", abbr = "i12iz4n"
Output: true
Explanation: The word "internationalization" can be abbreviated as "i12iz4n" ("i nternational iz atio n").


Example 2:

Input: word = "apple", abbr = "a2e"
Output: false
Explanation: The word "apple" cannot be abbreviated as "a2e".
"""

from functools import lru_cache


class Solution:
    # Time complexity: O(n+m)
    # Space complexity: O(1)
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = j = 0

        while i < len(word) and j < len(abbr):
            if word[i] == abbr[j]:
                i += 1
                j += 1
            elif abbr[j] == "0" or abbr[j].isalpha():
                return False
            else:
                split = 0
                while j < len(abbr) and abbr[j].isdigit():
                    split = split * 10 + int(abbr[j])
                    j += 1
                i += split

        return i == len(word) and j == len(abbr)


# Variant: wildcard (* matches any sequence of characters)
class SolutionVariant:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        @lru_cache(None)
        def dfs(i, j):
            # Base case: both pointers reach the end
            if i == len(word) and j == len(abbr):
                return True

            # If only one pointer reaches the end
            if j == len(abbr):
                return False

            # Case 1: Wildcard '*'
            if abbr[j] == "*":
                # '*' can match zero or more characters
                # Try all possible expansions
                for skip in range(0, len(word) - i + 1):
                    if dfs(i + skip, j + 1):
                        return True
                return False

            # Case 2: Letter match
            if abbr[j].isalpha():
                if i < len(word) and word[i] == abbr[j]:
                    return dfs(i + 1, j + 1)
                return False

            # Case 3: Number skip (no leading zeros)
            if abbr[j].isdigit():
                if abbr[j] == "0":  # invalid
                    return False
                num = 0
                while j < len(abbr) and abbr[j].isdigit():
                    num = num * 10 + int(abbr[j])
                    j += 1
                return dfs(i + num, j)

            return False

        return dfs(0, 0)
