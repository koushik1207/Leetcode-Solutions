def firstMissingPositive(self, nums: List[int]) -> int:
    num_list = [item for item in nums if item > 0]
    num_list = sorted(num_list)
    if num_list == []:
        return 1
    k = num_list[-1]
    for i in range(0,k+1):
        if i==0:
            continue
        if i == num_list[-1]:
            return(i+1)
            continue
        elif i not in num_list:
            return i
        else:
            continue