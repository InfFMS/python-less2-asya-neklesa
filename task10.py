# c столбец
# s строка
# c столбец
# s строка

s1 = int(input())
c1 = int(input())
s2 = int(input())
c2 = int(input())
def print_matrix(matrix):
    for i in range(len(matrix)):
        print(matrix[i])
if c1 > 8 or s1 > 7 or c2 > 8 or s2 > 8:
    print('no')
d = [[0]*8 for i in range(8)]
for k in range(0, 8):
    d[s1][k] = 1
    d[k][c1] = 1
    if s1 - k >= 0 and c1 - k >= 0:
        d[s1 - k][c1 - k] = 1
    if s1 + k < 8 and c1 + k < 8:
        d[s1 + k][c1 + k] = 1
    if s1 - k >= 0 and c1 + k < 8:
        d[s1 - k][k + c1] = 1
    if s1 + k < 8 and c1 - k >= 0:
        d[s1 + k][c1 - k] = 1
print_matrix(d)
if d[c2][s2] == 1:
    print('yes')
else:
    print('no')