def rearrange_word(word, indices):
    if len(word) != len(indices):
        raise ValueError("Length of word and indices must be the same")

    rearranged_list = []

    for idx in indices:
        rearranged_list.append(word[idx])

    rearranged_word = ''.join(rearranged_list)

    return rearranged_word


word = "example"
indices = [3, 1, 6, 5, 2, 0, 4]
result = rearrange_word(word, indices)
print(result)
