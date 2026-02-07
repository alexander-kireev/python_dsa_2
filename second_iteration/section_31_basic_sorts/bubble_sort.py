




def bubble_sort(nums):
    switched = True
    runs = 0

    while switched:
        switched = False

        for i in range(len(nums) - 1 - runs):
            if nums[i] > nums[i + 1]:
                switched = True
                nums[i], nums[i + 1] = nums[i + 1], nums[i]

        runs += 1
    
    return nums


l = [4, 6, 8, 1, 3, 2, 9]

print(bubble_sort(l))