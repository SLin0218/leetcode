from typing import List


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        m = {}
        for s in equations:
            lv = s[0]
            rv = s[3]
            if s[1] == "=":
                if lv in m:
                    m[lv].append(rv)
                else:
                    m[lv] = [rv]
                if rv in m:
                    m[rv].append(lv)
                else:
                    m[rv] = [lv]

        def lin(l, r, m, qc):
            if l in qc:
                return True
            qc.append(l)
            if l in m:
                if r in m[l]:
                    return False
                for h in m[l]:
                    if not lin(h, r, m, qc):
                        return False
            return True

        for s in equations:
            lv = s[0]
            rv = s[3]
            if s[1] == "!":
                if lv == rv:
                    return False
                vv = lin(lv, rv, m, [])
                if not vv:
                    return False
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

    equations = ["e!=c","b!=b","b!=a","e==d"]
    r = Solution().equationsPossible(equations)
    print(r)
