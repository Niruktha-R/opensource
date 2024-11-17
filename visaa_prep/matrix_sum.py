def compute_res_arr(matrix, n):
    A = []
    for i in range(n):
        sum_of_row = sum(matrix[i])
        sum_of_col = sum(matrix[j][i] for j in range(n))
        A.append(sum_of_row + sum_of_col)
    return A
n = int(input())
matx = [list(map(int, input().split())) for _ in range(n)]
res_arr = compute_res_arr(matx,n)
print(" ".join(map(str, res_arr)))
