# c столбец
# s строка
c1 = int(input())
s1 = int(input())
c2 = int(input())
s2 = int(input())

def print_matrix(matrix):
    for i in range(len(matrix)):
        print(matrix[i])

if c1 > 8 or s1 > 7 or c2 > 8 or s2 > 8:
    print('no')

d = [[0]*8 for i in range(8)]

for k in range(0, 8):
    d[c1][k] = 1
    d[k][s1] = 1
print_matrix(d)

if d[c2][s2] == (1, 1):
    print('yes')
else:
    print('no')
