"""
Given two sorted arrays nums1 and nums2 of size m and n respectively,
return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
"""

from typing import List


class Solution:
    # Time Complexity: O(log (m+n))
    # Space Complexity: O(1)
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # ensure nums1 is the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        low, high = 0, m

        while low <= high:
            midX = (low + high) // 2
            midY = (m + n + 1) // 2 - midX

            maxLeftX = float("-inf") if midX == 0 else nums1[midX - 1]
            minRightX = float("inf") if midX == m else nums1[midX]

            maxLeftY = float("-inf") if midY == 0 else nums2[midY - 1]
            minRightY = float("inf") if midY == n else nums2[midY]

            if maxLeftX <= minRightY and maxLeftY <= minRightX:
                if (m + n) % 2 == 0:
                    return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2
                else:
                    return max(maxLeftX, maxLeftY)
            elif maxLeftX > minRightY:
                high = midX - 1  # move left
            else:
                low = midX + 1  # move right
