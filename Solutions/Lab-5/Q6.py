def duplicates(L):
    for i in range(len(L) - 1):
        if L[i] == L[i + 1]:
            return True
    return False

# Test Case 1
L1 = [1, 2, 3]
print(duplicates(L1))

# Test Case 2
L1 = [1, 1, 3]
print(duplicates(L1))

# Test Case 3
L1 = [1, 2, 2]
print(duplicates(L1))