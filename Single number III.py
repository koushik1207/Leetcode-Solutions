class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        t = []
        for i in range(len(nums)):
            x = nums.pop(i)
            if x not in nums:
                t.append(x)
                if len(t)==2:
                    break
            nums.insert(i,x)
        return t