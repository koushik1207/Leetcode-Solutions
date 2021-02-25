class Solution:
    def arrangeWords(self, text: str) -> str:
        t = text.split(" ")
        t = sorted(t, key=len)
        res = ' '.join(t)
        res = res.capitalize()
        return(res)