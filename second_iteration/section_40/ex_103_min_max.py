def find_max_min(myList):
    nums = myList
    small = None
    big = None

    for num in nums:
        if big is None:
            big = num
        if small is None:
            small = num

        if num < small:
            small = num
        
        if num > big:
            big = num

    return (big, small)
    


print( find_max_min([5, 3, 8, 1, 6, 9]) )


"""
    EXPECTED OUTPUT:
    ----------------
    (9, 1)
    
"""