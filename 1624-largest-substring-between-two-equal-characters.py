class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        # 找到最左边的index,最右边的减最左边的,取最大值
        first_index = {}
        r = -1
        for i in range(len(s)):
            if s[i] in first_index:
                r = max(i - first_index[s[i]] - 1, r)
            else:
                first_index[s[i]] = i
        return r


if __name__ == "__main__":
    s = "aa"
    r = Solution().maxLengthBetweenEqualCharacters(s)
    print(r)

    s = "abca"
    r = Solution().maxLengthBetweenEqualCharacters(s)
    print(r)

    s = "cbzxy"
    r = Solution().maxLengthBetweenEqualCharacters(s)
    print(r)
