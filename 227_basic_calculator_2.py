"""
Given a string s which represents an expression, evaluate this expression and return its value.
The integer division should truncate toward zero.
You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().


Example 1:

Input: s = "3+2*2"
Output: 7


Example 2:

Input: s = " 3/2 "
Output: 1


Example 3:

Input: s = " 3+5 / 2 "
Output: 5
"""


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def calculate(self, s: str) -> int:
        if len(s) == 0:
            return 0

        current_number = 0
        last_number = 0
        result = 0
        operation = "+"

        for i, ch in enumerate(s):
            if ch.isdigit():
                current_number = current_number * 10 + int(ch)

            # When we hit an operator or end of string
            if not ch.isdigit() or i == len(s) - 1:
                if operation == "+":
                    result += last_number
                    last_number = current_number
                elif operation == "-":
                    result += last_number
                    last_number = -current_number
                elif operation == "*":
                    last_number = last_number * current_number
                elif operation == "/":
                    last_number = int(
                        last_number / current_number
                    )  # Truncate toward zero

                operation = ch
                current_number = 0

        result += last_number
        return result
