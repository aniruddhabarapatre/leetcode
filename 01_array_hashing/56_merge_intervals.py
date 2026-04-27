"""
Given an array of intervals where intervals[i] = [starti, endi],
merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

Example 3:

Input: intervals = [[4,7],[1,4]]
Output: [[1,7]]
Explanation: Intervals [1,4] and [4,7] are considered overlapping.
"""

from typing import List


class Solution:
    # Time complexity: O(n log n) for sorting, O(n) for merging
    # Space complexity: O(n) for the output list

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged = []
        intervals.sort(key=lambda x: x[0])  # Sort by start time

        for start, end in intervals:
            if not merged or merged[-1][1] < start:
                merged.append([start, end])  # No overlap, add new interval
            else:
                merged[-1][1] = max(merged[-1][1], end)  # Overlap, merge intervals
        return merged
