def twoSum(nums, target):
    output = []
    for a in range(len(nums)):
        for I in range(len(nums)-1, a ,-1):
            if nums[a] + nums[I] == target:
                output.append(a)
                output.append(I)
                break
        if len(output) == 2:
            break
    return output

print(twoSum([2, 7, 11, 15], 26))