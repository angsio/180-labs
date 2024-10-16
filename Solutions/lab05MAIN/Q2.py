def list_to_str(L):
    s = '['
    for i in L:
        if type(i) is str:
            s += f"'{i}', "
        else:
            s += f'{i}, '
    s = s[:-2]
    s += ']'
    return s

print(list_to_str([1, 2, 3, 'hello', True, [], (), {}]))