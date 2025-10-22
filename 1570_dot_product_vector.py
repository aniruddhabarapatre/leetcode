"""
Given two sparse vectors, compute their dot product.

Implement class SparseVector:

SparseVector(nums) - Initializes the object with the vector nums
dotProduct(vec) - Compute the dot product between the instance of SparseVector and vec

A sparse vector is a vector that has mostly zero values, you should store the sparse vector efficiently and compute the dot product between two SparseVector.

Follow up: What if only one of the vectors is sparse?

Example 1:

Input: nums1 = [1,0,0,2,3], nums2 = [0,3,0,4,0]
Output: 8
Explanation: v1 = SparseVector(nums1) , v2 = SparseVector(nums2)
v1.dotProduct(v2) = 1*0 + 0*3 + 0*0 + 2*4 + 3*0 = 8
"""

from typing import List


class SparseVector:
    # Time complexity: O(min(m, n)) where m and n are the number of non-zero elements in the two vectors
    # Space complexity: O(k) where k is the number of non-zero elements in the vector

    def __init__(self, nums: List[int]):
        # Store only non-zero values with their indices
        self.values = {i: num for i, num in enumerate(nums) if num != 0}

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: "SparseVector") -> int:
        # Iterate over smaller dictionary for efficiency
        if len(self.values) > len(vec.values):
            return vec.dotProduct(self)

        result = 0
        for i, val in self.values.items():
            if i in vec.values:
                result += val * vec.values[i]

        return result


# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
