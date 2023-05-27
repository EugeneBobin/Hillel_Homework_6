tuples = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
dictionary = {}
for key, value in tuples:
    if key in dictionary:
        dictionary[key].append(value)
    else:
        dictionary[key] = [value]
print(dictionary)
