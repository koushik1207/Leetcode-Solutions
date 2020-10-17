def addTwoNumbers(self, l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    num1 = list()
    num2 = list()
    t = t1 = 0
    while l1:
        num1.append(l1.val)
        l1 = l1.next
    while l2:
        num2.append(l2.val)
        l2 = l2.next
    for i in range(len(num1)):
        t = t + num1[i]*pow(10,i)
    for i in range(len(num2)):
        t1 = t1 + num2[i]*pow(10,i)
    ans = t+t1
    out = [int(d) for d in str(ans)]
    out = out[::-1]
    l3 = ListNode(out[0])
    head=l3
    for i in range(1,len(out)):
        new = ListNode(out[i])
        l3.next = new
        l3 = l3.next
    return head