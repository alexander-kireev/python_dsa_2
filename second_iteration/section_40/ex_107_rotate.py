

def rotate(nums, k):
    if not nums:
        return
    
    k = k % len(nums)

    if k == 0:
        return
    
    nums.reverse()

    for i in range(0, k // 2):
        temp = nums[i]
        nums[i] = nums[k - 1 - i]
        nums[k - 1 - i] = temp

    for i in range((len(nums) - k) // 2):
        temp = nums[k + i]
        nums[k + i] = nums[len(nums) - 1 - i]
        nums[len(nums) - 1 - i] = temp

    return

    

    


nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
rotate(nums, k)
print("Rotated array:", nums)


"""
    EXPECTED OUTPUT:
    ----------------
    Rotated array: [5, 6, 7, 1, 2, 3, 4]

"""