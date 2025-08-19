from typing import List


class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        l = len(nums)
        for i in range(l):
            if nums[start] == target:
                return 0
            if (start - i >= 0 and nums[start - i] == target) or (
                start + i < l and nums[start + i] == target
            ):
                return i
            i += 1
        return 0


if __name__ == "__main__":
    # case1 output 1
    nums = [1, 2, 3, 4, 5]
    target = 5
    start = 3
    r = Solution().getMinDistance(nums, target, start)
    print(r)

    # case2 output 0
    nums = [1]
    target = 1
    start = 0
    r = Solution().getMinDistance(nums, target, start)
    print(r)

    # case3
    nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    target = 1
    start = 0
    r = Solution().getMinDistance(nums, target, start)
    print(r)
