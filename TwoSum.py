def twoSum(self, nums, target):
	temp = set(nums)
	print(temp)
	output = list()
	same = target/2
	if nums.count(same) == 2:
		print(same)
		output.append(nums.index(same))
		nums.pop(nums.index(same))
		nums.insert(0,(target+1))
		output.append(nums.index(same))
	else:
		for i in range(len(nums)):
			x = target - nums[i]
			if x in temp:
				if nums.index(x) == i:
					continue
				else:
					output.append(i)
	return output