class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        currA, currB = headA, headB
        
        while currA != currB:
            currB = headA if currB is None else currB.next
            currA = headB if currA is None else currA.next
            
        return currA