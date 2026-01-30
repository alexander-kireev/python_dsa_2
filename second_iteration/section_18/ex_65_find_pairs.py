def find_pairs(arr1, arr2, target):
    pairs = []

    buddies = set()

    for num in arr1:
        buddies.add(target - num)

    for num in arr2:
        if num in buddies:
            pairs.append((target - num, num))    
    
    return pairs




arr1 = [1, 2, 3, 4, 5]
arr2 = [2, 4, 6, 8, 10]
target = 7
 
pairs = find_pairs(arr1, arr2, target)
print (pairs)