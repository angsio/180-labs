import numpy as np

def print_matrix(M_lol):
    print(M)

def get_lead_ind(row):
    for i in range(len(row)):
        if row[i] != 0:
            return i
    return len(row)

def get_row_to_swap(M, start_i):

    row_to_swap = start_i
    greatest_lead_ind = get_lead_ind(M[start_i])
    for i in range(start_i + 1, len(M)):
        if get_lead_ind(M[i]) < greatest_lead_ind:
            row_to_swap = i
            greatest_lead_ind = get_lead_ind(M[i])
    return row_to_swap

def add_rows_coefs(r1, c1, r2, c2):
    r1 = np.array(r1)
    r2 = np.array(r2)

    r = c1*r1 + c2*r2

    return r

def eliminate(M, row_to_sub, best_lead_ind):
    M = np.array(M)
    for i in range(row_to_sub + 1, len(M)):

        M[i] = add_rows_coefs(M[row_to_sub], -M[i][best_lead_ind], M[i], M[row_to_sub][best_lead_ind])

    return M

def forward_step(M):

    # Swapping Part
    for i in range(len(M) - 1):

        row_swap = get_row_to_swap(M, i)
        row_og = i

        M[row_og], M[row_swap] = M[row_swap], M[row_og]


        if M[i + 1][get_lead_ind(M[i])] != 0:
            M = eliminate(M, i, get_lead_ind(M[i]))

    return M

def backward_step(M):

    sols = np.zeros(len(M))

    for i in range(len(M) - 1, -1, -1):
      sols[i] = (M[i][-1] - np.dot(M[i][:-1], sols))/M[i][i]

    return sols

def solve(M, b):

    b = np.reshape(b, (len(M), 1))

    aug = np.append(M, b, 1)
    
    aug = forward_step(aug)
    sol = backward_step(aug)

    print(sol)
    print(np.dot(M, sol))



    

M = [[5, 6, 7, 8],
    [0, 3, 5, 2],
    [0, 2, 1, 1],
    [0, 0, 7, 0]]

M = np.array(M)

b = [2, 3, 4, 1]
b = np.array(b)

solve(M, b)








