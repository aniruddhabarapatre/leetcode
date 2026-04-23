"""
Given an integer array nums and an integer k, return the k most frequent elements within the array.

The test cases are generated such that the answer is always unique.

You may return the output in any order.

Example 1:

Input: nums = [1,2,2,3,3,3], k = 2
Output: [2,3]

Example 2:

Input: nums = [7,7], k = 1
Output: [7]

"""

from typing import List


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n)

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for _ in range(len(nums) + 1)]
        frequency = {}

        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1

        for num, freq in frequency.items():
            bucket[freq].append(num)
        result = []

        for i in range(len(bucket) - 1, 0, -1):
            for num in bucket[i]:
                result.append(num)
                if len(result) == k:
                    return result
