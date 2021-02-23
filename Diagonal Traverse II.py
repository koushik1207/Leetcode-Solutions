class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        res = {}
        out = []
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                #print(res.keys())
                if i+j in res.keys():
                    res[i+j].insert(0,nums[i][j])
                    continue
                res[i+j] = []
                res[i+j].insert(0,nums[i][j])
        print(res)
        for i in res.values():
            for x in i:
                out.append(x)
        return(out)