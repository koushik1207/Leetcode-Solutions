def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    a = nums1
    b = nums2
    if len(a)>len(b):
        a = nums2
        b = nums1
    x=len(a)
    y=len(b)
    start = 0
    end = x
    total = x + y
    while(start <= end):
        partition_x = (start+end)//2
        partition_y = (x+y+1)//2 - partition_x
        maxLeftX = float('-inf') if partition_x == 0 else a[partition_x-1]
        minRightX = float('inf') if partition_x == x else a[partition_x]
        maxLeftY = float('-inf') if partition_y == 0 else b[partition_y-1]
        minRightY = float('inf') if partition_y == y else b[partition_y]
        #print(partition_x,partition_y)
        if maxLeftX <= minRightY and maxLeftY <= minRightX:
            #print("start",start,"end",end)
            if (x+y)%2 == 0:
                k = max(maxLeftX,maxLeftY)+min(minRightX,minRightY)
                return k/2
            else:
                return max(maxLeftX,maxLeftY)
        elif maxLeftX > minRightY:
            end = partition_x - 1
        else:
            start = partition_x + 1