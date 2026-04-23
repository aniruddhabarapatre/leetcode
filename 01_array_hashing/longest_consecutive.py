from typing import List


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longestStreak = 0

        for num in numSet:
            if num - 1 not in numSet:
                currentNum = num
                currentStreak = 1

                while currentNum + 1 in numSet:
                    currentNum += 1
                    currentStreak += 1

                longestStreak = max(longestStreak, currentStreak)
        return longestStreak
