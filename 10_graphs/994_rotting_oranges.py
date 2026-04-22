"""
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

Example 1:

Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4

Example 2:

Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.

Example 3:

Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
"""

from collections import deque
from typing import List


class Solution:
    # Time complexity: O(m*n)
    # Space complexity: O(m*n)

    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        rotten = deque()
        fresh = 0

        # Initialize queue with all the rotten oranges and count the fresh oranges
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    rotten.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        # BFS
        minutes = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while rotten:
            r, c, time = rotten.popleft()
            minutes = max(minutes, time)

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    fresh -= 1
                    rotten.append((nr, nc, time + 1))

        # Check if all fresh oranges have rotted
        return minutes if fresh == 0 else -1
