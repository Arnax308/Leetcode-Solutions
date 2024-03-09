# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        val = []

        while head:

            val.append(head.val)
            head = head.next

        val.pop(-n)
        if len(val) >= 1:
            nhead = ListNode(val[0])
            dup = ListNode(-1)

            dup.next = nhead
            
            for i in range(1,len(val)):

                nhead.next = ListNode(val[i])
                nhead = nhead.next

        else:
            return 

        return dup.next