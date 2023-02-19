

def twoSum(nums, target):

    # map = {
    #   5: 1
    # }

    map = {}
    for i in range(len(nums)):
        if (target-nums[i]) in map:
            return [map[target-nums[i]], i]
        map[nums[i]] = i


print( twoSum([1, 2, 3,], 5) )
