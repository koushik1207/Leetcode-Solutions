def lengthOfLongestSubstring(self, s: str) -> int:
    if not s:
        return 0
    set ={}
    l,a=0,0
    
    for x in range(len(s)):
        if s[x] in set:
            l=max(l,1+set[s[x]])
        set[s[x]]=x
        a=max(a, x - l + 1)
        
    return a