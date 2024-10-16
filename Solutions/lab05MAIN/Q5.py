def match_pattern(L1, L2):
    if len(L2) > len(L1):
        return False
    else:
        for i in range(len(L1)):
            if L1[i:len(L2) + i] == L2:
                return True
        return False

# Test Case 1
L1 = [1, 2, 3, 4, 5]
L2 = [2, 3, 4]
print(match_pattern(L1, L2))

# Test Case 2
L1 = [1, 2, 3, 4, 5]
L2 = [1, 2, 3]
print(match_pattern(L1, L2))

# Test Case 3
L1 = [1, 2, 3, 4, 5]
L2 = [1, 2, 4]
print(match_pattern(L1, L2))

# Test Case 4
L1 = [1, 2, 3, 4, 5]
L2 = [1, 2, 4, 5, 6, 7]
print(match_pattern(L1, L2))

# Test Case 5
L1 = [1, 2, 3, 4, 5]
L2 = [3, 4, 5]
print(match_pattern(L1, L2))