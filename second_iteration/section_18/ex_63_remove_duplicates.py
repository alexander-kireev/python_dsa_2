def remove_duplicates(my_list):
    filtered = set()

    for num in my_list:
        filtered.add(num)
    
    return list(filtered)




my_list = [1, 2, 3, 4, 1, 2, 5, 6, 7, 3, 4, 8, 9, 5]

print(remove_duplicates(my_list))