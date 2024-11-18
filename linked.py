def smallest_lexicographical_string(new_order, word):
    return ''.join(sorted(word, key=dict(zip(new_order, range(len(new_order)))).get))
new_order = "bacdefghijklnmopqrstuvwxyz"
word = "hello"
smallest_string = smallest_lexicographical_string(new_order, word)
print(smallest_string)
