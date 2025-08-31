from typing import List


class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        # TODO
        return 0


if __name__ == "__main__":
    nums1 = [1, 4, 2]
    nums2 = [1, 2, 4]
    r = Solution().maxUncrossedLines(nums1, nums2)
    print(r)

    nums1 = [2, 5, 1, 2, 5]
    nums2 = [10, 5, 2, 1, 5, 2]
    r = Solution().maxUncrossedLines(nums1, nums2)
    print(r)

    nums1 = [1, 3, 7, 1, 7, 5]
    nums2 = [1, 9, 2, 5, 1]
    r = Solution().maxUncrossedLines(nums1, nums2)
    print(r)
