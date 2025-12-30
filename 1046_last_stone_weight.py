"""
You are given an array of integers stones where stones[i] represents the weight of the ith stone.

We want to run a simulation on the stones as follows:

At each step we choose the two heaviest stones, with weight x and y and smash them togethers
If x == y, both stones are destroyed
If x < y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
Continue the simulation until there is no more than one stone remaining.

Return the weight of the last remaining stone or return 0 if none remain.

Example 1:

Input: stones = [2,3,6,2,4]
Output: 1
Explanation:
We smash 6 and 4 and are left with a 2, so the array becomes [2,3,2,2].
We smash 3 and 2 and are left with a 1, so the array becomes [1,2,2].
We smash 2 and 2, so the array becomes [1].

Example 2:

Input: stones = [1,2]
Output: 1
"""

from typing import List
import heapq


class Solution:
    # Time Complexity: O(n log n) where n is the number of stones
    # Space Complexity: O(n)
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Convert all weights to negative values to simulate a max heap using heapq
        max_heap = [-stone for stone in stones]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            # Pop the two heaviest stones (most negative values)
            first = -heapq.heappop(max_heap)
            second = -heapq.heappop(max_heap)

            if first != second:
                # If they are not equal, push the difference back into the heap
                heapq.heappush(max_heap, -(first - second))

        # If there's a stone left, return its weight, otherwise return 0
        return -max_heap[0] if max_heap else 0
