def get_matrix(n, m, values):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(values)
    return matrix

print(get_matrix(4, 2, 13))
