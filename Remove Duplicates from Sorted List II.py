class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None: return head
        l = set()
        temp = head
        while temp and temp.next:
            if temp.val == temp.next.val:
                l.add(temp.val)
            temp = temp.next
        dum = ListNode(0)
        dum.next = head
        temp = dum
        while temp and temp.next:
            if temp.next.val in l:
                temp.next = temp.next.next
            else:
                temp = temp.next
        return dum.next