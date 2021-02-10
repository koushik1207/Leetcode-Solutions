class Solution(object):
    def isAnagram(self, s, t):
        x = {}
        m = {}
        for i in s:
            if i not in x:
                x[i] = 1
            else:
                x[i] = x.get(i) + 1
        for i in t:
            if i not in m:
                m[i] = 1
            else:
                m[i] = m.get(i) + 1
        if m.keys() == x.keys() and m.values() == x.values():
            return True
        else:
            return False