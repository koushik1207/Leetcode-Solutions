class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        x = nums[len(nums)-k:len(nums)]
        del nums[len(nums)-k:len(nums)]
        nums[:0]= x