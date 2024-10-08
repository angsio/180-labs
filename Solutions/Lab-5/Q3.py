def lists_are_the_same(L1, L2):
    if len(L1) != len(L2):
        return False
    else:
        for i in range(len(L1)):
            if L1[i] == L2[i]:
                pass
            else:
                return False
        return True

L1 = [1, 2, 3]
L2 = [1, 2, 3]
print(lists_are_the_same(L1, L2))
L1 = [1, 2, 3]
L2 = [2, 2, 3]
print(lists_are_the_same(L1, L2))