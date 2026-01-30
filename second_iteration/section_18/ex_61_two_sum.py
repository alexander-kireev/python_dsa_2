def two_sum(nums, target):

    found = {}

    for i in range(len(nums)):
        buddy = target - nums[i]

        if buddy in found:
            return [found[buddy], i]
        else:
            found[nums[i]] = i


    return []

nums = [5, 1, 7, 2, 9, 3]
target = 10


print(two_sum(nums, target))