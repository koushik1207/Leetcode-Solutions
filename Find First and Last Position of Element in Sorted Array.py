class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = -1
        end = -1
        for i in range(len(nums)):
            if nums[i] == target:
                if start == -1:
                    start = i
                    end = i
                else:
                    end = i
        res = []
        res.append(start)
        res.append(end)
        return res
            