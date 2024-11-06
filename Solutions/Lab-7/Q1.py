L = [[1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]

def change():
    L[0] = 0

def change2():
    L[0][0] = 0

change2()
print(L)

change()
print(L)
