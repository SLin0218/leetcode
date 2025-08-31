from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        s = "[" + str(self.val)
        next = self.next
        while next:
            s += ", " + str(next.val)
            next = next.next
        s += "]"
        return s


# 转换为数字求和
# class Solution:
#     def addTwoNumbers(
#         self, l1: Optional[ListNode], l2: Optional[ListNode]
#     ) -> Optional[ListNode]:
#         def toNumber(l: Optional[ListNode], rank: int) -> int:
#             if l:
#                 p = 0
#                 if l.next:
#                     p = toNumber(l.next, rank * 10)
#                 return (rank * l.val) + p
#             return 0
#
#         def toListNode(n: int) -> Optional[ListNode]:
#             next = None
#             if n > 0:
#                 next = toListNode(n // 10)
#                 return ListNode(n % 10, next)
#             return None
#         sum = toNumber(l1, 1) + toNumber(l2, 1)
#         if sum == 0:
#             return ListNode(0, None)
#         return toListNode(sum)


# 直接递归求和
class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        def sum(
            l1: Optional[ListNode], l2: Optional[ListNode], carry: int
        ) -> Optional[ListNode]:
            """
            carry: 进位
            """
            if l1 or l2:
                l1_value = 0
                l2_value = 0
                next1 = None
                next2 = None
                if l1:
                    l1_value = l1.val
                    next1 = l1.next
                if l2:
                    l2_value = l2.val
                    next2 = l2.next
                ss = l1_value + l2_value + carry
                return ListNode(ss % 10, sum(next1, next2, ss // 10))
            if carry > 0:
                return ListNode(carry, None)
            return None

        return sum(l1, l2, 0)


if __name__ == "__main__":
    l1 = ListNode(2, ListNode(4, ListNode(3, None)))
    l2 = ListNode(5, ListNode(6, ListNode(4, None)))
    r = Solution().addTwoNumbers(l1, l2)
    print(r)

    l1 = ListNode(0, None)
    l2 = ListNode(0, None)
    r = Solution().addTwoNumbers(l1, l2)
    print(r)

    l1 = ListNode(
        9,
        ListNode(
            9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, None)))))
        ),
    )
    l2 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, None))))
    r = Solution().addTwoNumbers(l1, l2)
    print(r)
