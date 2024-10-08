from xmlrpc.client import FastMarshaller


def list1_sw_list2(L1, L2):
    if len(L2) > len(L1):
        return False
    else:
        for i in range(len(L2)):
            if L2[i] == L1[i]:
                pass
            else:
                return False
        return True

# Test Case 1
L1 = [1, 2, 3, 4, 5]
L2 = [1, 2, 3]
print(list1_sw_list2(L1, L2))

# Test Case 2
L1 = [1, 2, 3, 4, 5]
L2 = [1, 2, 3, 4, 5]
print(list1_sw_list2(L1, L2))

# Test Case 3
L1 = [1, 2, 3, 4]
L2 = [1, 2, 3, 4, 5]
print(list1_sw_list2(L1, L2))

# Test Case 4
L1 = [2, 2, 3, 4, 5]
L2 = [1, 2, 3]
print(list1_sw_list2(L1, L2))

# Test Case 5
L1 = [4, 1, 2, 3, 5]
L2 = [1, 2, 3]
print(list1_sw_list2(L1, L2))