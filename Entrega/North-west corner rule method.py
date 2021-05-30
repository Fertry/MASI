des = [[2, 3, 4, 5],
       [3, 4, 5, 6],
       [3, 4, 5, 6],
       [4, 5, 6, 7]]

supp = [20, 20, 30, 10]
deman = [15, 35, 15, 10]
col = [0, 0, 0, 0]
row = [0, 0, 0, 0]
rows = 4
columns = 4
ans = 0
for i in range(0, columns):
    for j in range(0, rows):
        if col[i] == 1 or row[j] == 1:
            continue
        m = min(supp[i], deman[j])
        supp[i] = supp[i] - m
        deman[j] = deman[j] - m
        ans = ans + des[i][j] * m
        if deman[j] == 0:
            row[j] = 1
        if supp[i] == 0:
            col[i] = 1

print(ans)