"""
You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. 
You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

Example 2:

Input: nums = [1], k = 1
Output: [1]
 
"""
from typing import List
from collections import deque

class Solution:
    # Time complexity: O(n)
    # Space complexity: O(k)
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)

        if n * k == 0:
            return []

        if k == 1:
            return nums

        dq = deque()  # stores indices
        result = []

        for i in range(len(nums)):
            # Remove indices out of current window
            if dq and dq[0] == i - k:
                dq.popleft()

            # Maintain decreasing order: remove smaller elements from back
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()

            dq.append(i)

            # Add max (front of deque) to result once we hit window size k
            if i >= k - 1:
                result.append(nums[dq[0]])

        return result
            
        