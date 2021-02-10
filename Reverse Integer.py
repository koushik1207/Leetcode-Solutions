class Solution:
    def reverse(self, x: int) -> int:
        ans=int(str(abs(x))[-1::-1]) if x>=0 else -1*int(str(abs(x))[-1::-1])
        return ans if ans>-1*2**31 and ans<2**31-1 else 0