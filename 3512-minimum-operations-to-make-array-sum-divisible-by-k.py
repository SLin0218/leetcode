from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        sum_nums = sum(nums)
        if sum_nums == k:
            return 0
        x = sum_nums % k
        if sum_nums < k:
            return sum_nums
        return x


if __name__ == "__main__":
    # case1
    nums = [3, 9, 7]
    k = 5
    r = Solution().minOperations(nums, k)
    print(r)

    # case2
    nums = [4, 1, 3]
    k = 4
    r = Solution().minOperations(nums, k)
    print(r)

    # case 3
    nums = [3, 2]
    k = 6
    # 1 1 3 4 10
    r = Solution().minOperations(nums, k)
    print(r)
