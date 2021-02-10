class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        if not root:
            return 0     
        temp = []
        if root.val>=low and root.val<=high:
            temp.append(root.val)
        if root.left:
            temp.append(self.rangeSumBST(root.left,low,high))
        if root.right:
            temp.append(self.rangeSumBST(root.right,low,high))
        
        return sum(temp) 