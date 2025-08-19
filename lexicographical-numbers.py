from typing import List


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        if n < 10:
            return [i for i in range(1, n + 1)]
        nums = []
        for h in range(1, 10):
            self.dfs(n, h, nums)
        return nums

    def dfs(self, n: int, i: int, nums: List[int]):
        nums.append(i)
        for h in range(0, 10):
            w = i * 10 + h
            if w <= n:
                self.dfs(n, w, nums)


if __name__ == "__main__":
    # case1
    n = 1000
    r = Solution().lexicalOrder(n)
    print(r)

    # case2
    n = 1009210
    r = Solution().lexicalOrder(n)
    print(r)
