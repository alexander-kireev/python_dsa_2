


def first_non_repeating_char(text):
    chars = {}
    
    for char in text:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    
    for char in text:
        if chars[char] == 1:
            return char



t = "leetcode"


print(first_non_repeating_char(t))

