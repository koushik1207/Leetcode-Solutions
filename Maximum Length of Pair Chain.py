class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda items: items[1])
        x = float('-inf') 
        res = 0
        for i in pairs:
            if x < i[0]:
                x = i[1]
                res+=1
        return(res)
        