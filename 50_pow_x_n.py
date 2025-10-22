"""
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

Example 1:

Input: x = 2.00000, n = 10
Output: 1024.00000
Example 2:

Example 2:

Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
"""


class Solution:
    # Time Complexity: O(log n)
    # Space Complexity: O(1)
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0

        if n < 0:
            x = 1 / x
            n = -n

        result = 1.0
        while n:
            if n % 2:  # if n is odd
                result *= x
            x *= x  # square the base
            n //= 2  # halve the exponent

        return result

    # Recursive approach
    """
    # Time complexity: O(n)
    # Space complexity: O(1)

        if n == 0:
            return 1.0

        if n < 0:
            return 1 / pow(x, -n)

        return x * pow(x, n - 1)
    """
