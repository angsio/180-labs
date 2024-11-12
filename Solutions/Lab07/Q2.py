L = [[1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]

def change(L):
    L2 = L[:]
    L2[0] = [0, 0]
    print(L2)

change(L)
print(L)