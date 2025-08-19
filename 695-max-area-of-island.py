from typing import List


class Solution:

    # up down left right
    neighbour = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        seen = set()
        n = 0
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                v = self.bfs(grid, x, y, seen)
                n = max(n, v)
        return n

    def bfs(self, grid: List[List[int]], x: int, y: int, seen: set):
        if (x, y) in seen:
            return 0
        seen.add((x, y))
        if grid[y][x]:
            nums = 1
            for i in range(4):
                xx = self.neighbour[i][1] + x
                yy = self.neighbour[i][0] + y
                if self.is_vaild_range(grid, xx, yy):
                    nums += self.bfs(grid, xx, yy, seen)
            return nums
        return 0

    def is_vaild_range(self, grid: List[List[int]], x: int, y: int):
        return 0 <= y < len(grid) and 0 <= x < len(grid[0])


if __name__ == "__main__":
    # case1
    grid = [
        [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
    ]
    r = Solution().maxAreaOfIsland(grid)
    print(r)

    # case2
    grid = [
        [1, 1, 0, 0, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 0, 1, 1],
        [0, 0, 0, 1, 1],
    ]
    r = Solution().maxAreaOfIsland(grid)
    print(r)

    grid = [
        [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
    ]

    r = Solution().maxAreaOfIsland(grid)
    print(r)
