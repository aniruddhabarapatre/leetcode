"""
You are given two strings order and s. All the characters of order are unique and were sorted in some custom order previously.
Permute the characters of s so that they match the order that order was sorted. More specifically,
if a character x occurs before a character y in order, then x should occur before y in the permuted string.

Return any permutation of s that satisfies this property.

Example 1:

Input: order = "cba", s = "abcd"
Output: "cbad"
Explanation: "a", "b", "c" appear in order, so the order of "a", "b", "c" should be "c", "b", and "a".
Since "d" does not appear in order, it can be at any position in the returned string. "dcba", "cdba", "cbda" are also valid outputs.

Example 2:

Input: order = "bcafg", s = "abcd"
Output: "bcad"
Explanation: The characters "b", "c", and "a" from order dictate the order for the characters in s.
The character "d" in s does not appear in order, so its position is flexible.
Following the order of appearance in order, "b", "c", and "a" from s should be arranged as "b", "c", "a".
"d" can be placed at any position since it's not in order.
The output "bcad" correctly follows this rule. Other arrangements like "dbca" or "bcda" would also be valid,
as long as "b", "c", "a" maintain their order.
"""


class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def customSortString(self, order: str, s: str) -> str:
        order_index = {}
        s_permutation = []

        for char in s:
            order_index[char] = order_index.get(char, 0) + 1

        for char in order:
            # Elem to be Ordered
            if char in order_index:
                s_permutation.append(char * order_index[char])
                del order_index[char]

        for unordered_elem in order_index:
            s_permutation.append(unordered_elem * order_index[unordered_elem])

        return "".join(s_permutation)
