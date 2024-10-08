def get_nums(L):
    return [L[i][1] for i in range(len(L))]

L = [["CIV", 92],
["180", 98],
["103", 99],
["194", 95]]

print(get_nums(L))