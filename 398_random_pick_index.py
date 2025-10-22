"""
Given an integer array nums with possible duplicates, randomly output the index of a given target number.
You can assume that the given target number must exist in the array.

Implement the Solution class:

    - Solution(int[] nums) -- Initializes the object with the array nums.
    - int pick(int target) -- Picks a random index i from nums where nums[i] == target.
        If there are multiple valid i's, then each index should have an equal probability of returning.


Example 1:

Input: ["Solution", "pick", "pick", "pick"]
        [[[1, 2, 3, 3, 3]], [3], [1], [3]]

Output: [null, 4, 0, 2]

Explanation
Solution solution = new Solution([1, 2, 3, 3, 3]);
solution.pick(3); // It should return either index 2, 3, or 4 randomly. Each index should have equal probability of returning.
solution.pick(1); // It should return 0. Since in the array only nums[0] is equal to 1.
solution.pick(3); // It should return either index 2, 3, or 4 randomly. Each index should have equal probability of returning.
"""

import random


class Solution:
    # Time Complexity: O(n) for initialization, O(1) for pick
    # Space Complexity: O(n)
    def __init__(self, nums: list[int]):
        self.indices = {}
        for i, n in enumerate(nums):
            if n not in self.indices:
                self.indices[n] = []
            self.indices[n].append(i)

    def pick(self, target: int) -> int:
        return random.choice(self.indices[target])


# Variant: Using Reservoir Sampling
class Solution2:
    # Time Complexity: O(n) for pickK
    # Space Complexity: O(1)
    def __init__(self, nums: list[int]):
        self.nums = nums

    # Step 1: fill initial k
    def pickK(self, k: int) -> list[int]:
        reservoir = self.nums[:k]
        n = len(self.nums)

        # Step 2: reservoir sampling
        for i in range(k, n):
            j = random.randint(0, i)
            if j < k:
                reservoir[j] = self.nums[i]

        return reservoir
