# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return None

        def mergeTwoList(listA, listB):
            dummy = ListNode(0)
            cur = dummy
            while listA and listB:
                if listA.val < listB.val:
                    cur.next = ListNode(listA.val)
                    cur = cur.next
                    listA = listA.next
                else:
                    cur.next = ListNode(listB.val)
                    cur = cur.next
                    listB = listB.next

            cur.next = listA or listB

            return dummy.next


        N = len(lists) - 1
        i, j = 0, N
        while i < j:
            lists[i] = mergeTwoList(lists[i], lists[j])
            i += 1
            j -= 1

            if i >= j:
                i = 0


        return lists[0]
