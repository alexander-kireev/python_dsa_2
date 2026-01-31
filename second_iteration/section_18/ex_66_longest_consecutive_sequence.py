def longest_consecutive_sequence(nums):
    nums_set = set(nums)
    
    longest_seq_len = 0

    for num in nums_set:
        if num - 1 not in nums_set:
            current_seq_len = 1
            
            while num + 1 in nums_set:
                num = num + 1
                current_seq_len += 1

            longest_seq_len = max(longest_seq_len, current_seq_len)

    return longest_seq_len

print( longest_consecutive_sequence([100, 4, 200, 1, 3, 2, 300, 400, 500]) )