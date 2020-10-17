import heapq
def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    
    res=[]
    intr= sorted(intervals)
    if intr==None:
        return None
    for item in intr:
        #print(res[-1][1])
        if not res or item[0]> res[-1][1]:
            res.append(item)
            #print(res)
        else:
            res[-1][1]=max(item[1],res[-1][1])
            
    return res