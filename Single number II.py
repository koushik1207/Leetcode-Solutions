class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            x = nums.pop(i)
            if x not in nums:
                return x
            nums.insert(i,x)