d = [[3, -9, -8], [2, 4, 3]]
c = [[7, -3], [-2, 3], [6, 2]]
a = [[1, 2], [3, 4]]
b = [[5, 6], [7, 8]]
matAR = [[1, 2], [3, 4]]
matBR = [[5, 7], [6, 8]]

x = [[sum(a*b for a, b in zip(matA, matB))
      for matB in matBR] for matA in matAR]

# use the tuple() function to display a readable version of the result:

print(x)

#dot_matrix = [[sum(a*b for a, b in zip(matA_row, matB_col)) for matB_col in zip(*matB)] for matA_row in matA]
