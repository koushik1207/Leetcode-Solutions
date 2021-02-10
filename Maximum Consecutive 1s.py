class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        final = 0
        for i in nums:
            if i == 1:
                count = count+1
                print(count)
            else:
                print(count)
                if count > final:
                    final = count
                count = 0
            if count > final:
                final = count
        return final