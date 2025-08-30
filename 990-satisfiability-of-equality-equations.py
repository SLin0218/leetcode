from typing import List

# dps 使用深度优先搜索图
# class Solution:
#     def equationsPossible(self, equations: List[str]) -> bool:
#         m = {}
#         for s in equations:
#             left = s[0]
#             right = s[3]
#             if s[1] == "=":
#                 if left in m:
#                     m[left].append(right)
#                 else:
#                     m[left] = [right]
#                 if right in m:
#                     m[right].append(left)
#                 else:
#                     m[right] = [left]
#             # 已经遍例过
#             if left in qc:
#                 return True
#             qc.append(left)
#             if left in d:
#                 if right in d[left]:
#                     return False
#                 for h in m[left]:
#                     if not dfs(h, right, d, qc):
#                         return False
#             return True
#
#         for s in equations:
#             left = s[0]
#             right = s[3]
#             if s[1] == "!":
#                 if left == right:
#                     return False
#                 if not dfs(left, right, m, []):
#                     return False
#         return True


# Union Find 并查集数据结构
class UnionFind:
    def __init__(self) -> None:
        self.uf = [i for i in range(26)]

    # 递归查找到根节点返回 根节点的父节点等于自身
    def find(self, x):
        if self.uf[x] != x:
            # 路径压缩, 沿途所有节点指向根节点
            self.uf[x] = self.find(self.uf[x])
        return self.uf[x]

    # 找到a元素的根节点 指向新的根 b 合并两个集合
    def union(self, a: int, b: int):
        self.uf[self.find(a)] = self.find(b)


class Solution:

    def equationsPossible(self, equations: List[str]) -> bool:
        def toInt(s: str):
            return ord(s[0]) - 97

        union_find = UnionFind()
        for s in equations:
            if s[1] == "=":
                union_find.union(toInt(s[0]), toInt(s[3]))
        for s in equations:
            if s[1] == "!":
                if union_find.find(toInt(s[0])) == union_find.find(toInt(s[3])):
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

    equations = ["e!=c", "b!=b", "b!=a", "e==d"]
    r = Solution().equationsPossible(equations)
    print(r)
