"""
You are given an array of CPU tasks tasks, where tasks[i] is an uppercase english character from A to Z.
You are also given an integer n.
Each CPU cycle allows the completion of a single task, and tasks may be completed in any order.
The only constraint is that identical tasks must be separated by at least n CPU cycles, to cooldown the CPU.

Return the minimum number of CPU cycles required to complete all tasks.

Example 1:

Input: tasks = ["X","X","Y","Y"], n = 2
Output: 5
Explanation: A possible sequence is: X -> Y -> idle -> X -> Y.

Example 2:

Input: tasks = ["A","A","A","B","C"], n = 3
Output: 9
Explanation: A possible sequence is: A -> B -> C -> Idle -> A -> Idle -> Idle -> Idle -> A.
"""

from typing import List


class Solution:
    # Time Complexity: O(m) where m is the number of tasks
    # Space Complexity: O(1) since the size of the frequency array is fixed (26)
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Frequency array to count occurrences of each task
        freq = [0] * 26
        for task in tasks:
            freq[ord(task) - ord("A")] += 1

        max_freq = max(freq)
        max_count = freq.count(max_freq)

        # Calculate the minimum intervals needed
        part_count = max_freq - 1
        part_length = n - (max_count - 1)
        empty_slots = part_count * part_length
        available_tasks = len(tasks) - (max_freq * max_count)
        idles = max(0, empty_slots - available_tasks)

        return len(tasks) + idles
