def group_anagrams(words_list):
    collections = []

    # check each word
    for word in words_list:
        letters = {}

        has_collection = False

        for letter in word:
            if letter not in letters:
                letters[letter] = 1
            else:
                letters[letter] += 1
        
        for collection in collections:
            if collection["letters"] == letters:
                collection["words"].append(word)
                has_collection = True

        if not has_collection:
            collection = {}
            collection["letters"] = letters
            collection["words"] = [word]
            collections.append(collection)
        
       
    output = []

    for collection in collections:
        output.append(collection["words"])

    return output



def group_anagrams_2(words_list):
    anagrams = {}

    for word in words_list:
        sorted_word = "".join(sorted(word))

        if sorted_word not in anagrams:
            anagrams[sorted_word] = [word]
        else:
            anagrams[sorted_word].append(word)
    output = []
    for anagram in anagrams:
        output.append(anagrams[anagram])
        
    return output


print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

