"""
Given a Circular Linked List node, which is sorted in non-descending order,
write a function to insert a value insertVal into the list such that it remains a sorted circular list.
The given node can be a reference to any single node in the list and may not necessarily be the smallest value in the circular list.

If there are multiple suitable places for insertion, you may choose any place to insert the new value.
After the insertion, the circular list should remain sorted.

If the list is empty (i.e., the given node is null),
you should create a new single circular list and return the reference to that single node.
Otherwise, you should return the originally given node.

Example 1:

Input: head = [3,4,1], insertVal = 2
Output: [3,4,1,2]
Explanation: In the figure above, there is a sorted circular list of three elements.
You are given a reference to the node with value 3, and we need to insert 2 into the list.
The new node should be inserted between node 1 and node 3.
After the insertion, the list should look like this, and we should still return node 3.
"""

from typing import Optional


class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def insert(self, head: "Optional[Node]", insertVal: int) -> "Node":
        new_node = Node(insertVal)

        # Empty list
        if not head:
            new_node.next = new_node
            return new_node

        prev, curr = head, head.next

        while True:
            # Case 1: Normal ascending place
            if prev.val <= insertVal <= curr.val:
                break

            # Case 2: Rotation point (max -> min)
            if prev.val > curr.val:
                # insertVal is new max or new min
                if insertVal >= prev.val or insertVal <= curr.val:
                    break

            prev, curr = curr, curr.next

            # If we've gone full circle (no suitable place found)
            if prev == head:
                break

        # Insert node
        prev.next = new_node
        new_node.next = curr

        return head
