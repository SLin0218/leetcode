from typing import List


class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        around_m = [ [-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1] ]
        result = []
        rl = len(img)
        for r in range(rl):
            cl = len(img[r])
            result.append([0] * cl)
            for c in range(cl):
                result[r][c] = img[r][c]
                count = 1
                for i in range(8):
                    rr = r + around_m[i][0]
                    cc = c + around_m[i][1]
                    if 0 <= rr < rl and 0 <= cc < cl:
                        result[r][c] += img[rr][cc]
                        count += 1
                result[r][c] = result[r][c] // count
        return result


if __name__ == "__main__":
    output = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    img = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    r = Solution().imageSmoother(img)
    print(r)

    output = [[137, 141, 137], [141, 138, 141], [137, 141, 137]]
    img = [[100, 200, 100], [200, 50, 200], [100, 200, 100]]
    r = Solution().imageSmoother(img)
    print(r)
