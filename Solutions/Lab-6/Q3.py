def get_nums(L):
    return [L[i][1] for i in range(len(L))]

def lookup(L, num):
    nums_L = get_nums(L)
    try:
        i = nums_L.index(num)
        return L[i][0]
    except:
        return None

L = [["CIV", 92],
["180", 98],
["103", 99],
["194", 95]]

# Test Case 1
print(lookup(L, 99))

# Test Case 2
print(lookup(L, 95))

# Test Case 3
print(lookup(L, 10000))