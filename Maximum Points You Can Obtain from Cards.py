class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        if cardPoints is None:
            return 0
        now = sum(cardPoints[:k])
        res = now
        for i in range(1,k+1):
            now = now +  cardPoints[-i] - cardPoints[k-i]
            res = max(now,res)
        
        return res