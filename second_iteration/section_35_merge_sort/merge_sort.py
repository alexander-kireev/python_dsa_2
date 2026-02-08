def merge(list_1, list_2):
    merged = []
    i = 0
    j = 0

    while i < len(list_1) and j < len(list_2):

        if list_1[i] <= list_2[j]:
            merged.append(list_1[i])
            i += 1
        else:
            merged.append(list_2[j])
            j += 1

    while i < len(list_1):
        merged.append(list_1[i])
        i += 1
    
    while j < len(list_2):
        merged.append(list_2[j])
        j += 1

    return merged

def merge_sort(my_list):
    if len(my_list) <= 1:
        return my_list
    
    mid = len(my_list) // 2

    left = merge_sort(my_list[:mid])
    right = merge_sort(my_list[mid:])

    return merge(left, right)

l1 = [4, 8, 12, 19, 99]
l2 = [3, 5, 22, 30]

l3 = [19, 4, 7, 22, 14, 20, 19, 88]

print(merge_sort(l3))
