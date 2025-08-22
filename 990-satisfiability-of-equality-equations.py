from typing import List


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        m = [[0 for _ in range(26)] for _ in range(26)]
        for s in equations:
            lv = ord(s[0]) - 97
            rv = ord(s[3]) - 97
            if s[1] == "=":
                m[lv][rv] = 1
                m[rv][lv] = 1
        for mm in m:
            print(mm)
        return True


if __name__ == "__main__":
    # case1
    equations = ["a==b", "b!=a"]
    r = Solution().equationsPossible(equations)
    print(r)

    # case2
    equations = ["b==a", "a==b"]
    r = Solution().equationsPossible(equations)
    print(r)

    # case 3
    equations = ["a==b", "b!=c", "c==a"]
    r = Solution().equationsPossible(equations)
    print(r)

    # case 4
    equations = ["c==c", "b==d", "x!=z"]
    r = Solution().equationsPossible(equations)
    print(r)

    # case 5
    equations = ["a==b", "e==c", "b==c", "a!=e"]
    r = Solution().equationsPossible(equations)
    print(r)
