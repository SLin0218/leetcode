from typing import List

"""
[]
[0, 1]                             <= 0 + 1
[0, 1, 2]                          <= 2 + 1
[0, 1, 2, 3, 4, 5]                 <= 5 + 1
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]     <= 9 + 1
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
"""


class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        coins.sort()
        x = 1
        for coin in coins:
            # 如果当前硬币面值大于上一次(x+1) 则中间会无法被填充满
            if coin > x:
                return x
            x += coin
        return x


if __name__ == "__main__":
    # case1
    coins = [1, 3]
    r = Solution().getMaximumConsecutive(coins)
    print(r)

    # case2
    coins = [1, 1, 1, 4]
    r = Solution().getMaximumConsecutive(coins)
    print(r)

    # case 3
    coins = [1, 4, 10, 3, 1]
    # 1 1 3 4 10
    r = Solution().getMaximumConsecutive(coins)
    print(r)
