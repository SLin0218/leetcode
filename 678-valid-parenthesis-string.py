class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == "(":
                stack.append(c)
            elif c == ")":
                if len(stack) == 0:
                    return False
                stack.pop()
            else:
                # ()*
                if stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(c)
        print(stack)
        return True


if __name__ == "__main__":
    s = "()"
    r = Solution().checkValidString(s)
    print(r)

    s = "(*)"
    # ( ) (() ())
    r = Solution().checkValidString(s)
    print(r)

    s = "(*))"
    # ( )) (()) ()))
    r = Solution().checkValidString(s)
    print(r)
