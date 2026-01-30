


def find_duplicates(nums):

    found = {}

    duplicates = []

    for i in nums:
        if i in found:

            if found[i] == 1:
                duplicates.append(i)

            found[i] += 1
        else:
            found[i] = 1



    return duplicates

nums = [4, 3, 2, 7, 8, 2, 3, 1, 1, 1, 1]

print(find_duplicates(nums))

