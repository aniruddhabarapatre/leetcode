"""
Hercy wants to save money for his first car. He puts money in the Leetcode bank every day.

He starts by putting in $1 on Monday, the first day. Every day from Tuesday to Sunday,
he will put in $1 more than the day before. On every subsequent Monday, he will put in $1 more than the previous Monday.

Given n, return the total amount of money he will have in the Leetcode bank at the end of the nth day.

Example 1:

Input: n = 4
Output: 10
Explanation: After the 4th day, the total is 1 + 2 + 3 + 4 = 10.

Example 2:

Input: n = 10
Output: 37
Explanation: After the 10th day, the total is (1 + 2 + 3 + 4 + 5 + 6 + 7) + (2 + 3 + 4) = 37.
Notice that on the 2nd Monday, Hercy only puts in $2.

Example 3:

Input: n = 20
Output: 96
Explanation: After the 20th day, the total is (1 + 2 + 3 + 4 + 5 + 6 + 7) + (2 + 3 + 4 + 5 + 6 + 7 + 8) + (3 + 4 + 5 + 6 + 7 + 8) = 96.
"""


class Solution:
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def totalMoney(self, n: int) -> int:
        weeks = n // 7
        days = n % 7
        total = 0

        # Sum for complete weeks
        for week in range(weeks):
            week_start = week + 1
            total += sum(week_start + day for day in range(7))

        # Sum for remaining days
        week_start = weeks + 1  # Next week's starting amount
        for day in range(days):
            total += week_start + day

        return total

    # triangle number formula
    """
    def triSum(self, n: int) -> int:
        return (n * (n + 1)) >> 1

    def totalMoney3(self, days: int) -> int:
        nWeeks, rDays = divmod(days, 7)
        return self.triSum(days) - 42 * self.triSum(nWeeks - 1) - 6 * nWeeks * rDays
    """
