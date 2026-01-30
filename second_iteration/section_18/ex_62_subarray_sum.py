def subarray_sum(nums, target):
    prefix_sums = {0: -1}   # base case: sum 0 before starting
    current_sum = 0

    for i, num in enumerate(nums):
        current_sum += num
        if (current_sum - target) in prefix_sums:
            start = prefix_sums[current_sum - target] + 1
            return [start, i]
        prefix_sums[current_sum] = i

    return []


nums = [1, 2, 3, 4, 5]
target = 7
print(subarray_sum(nums, target))  # should print [1, 3]
