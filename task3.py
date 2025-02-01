
a = int(input())
if 1 < a % 10 < 5 and (a < 5 or a > 11):
    print(a, 'года')
elif a % 10 == 1 and a != 11:
    print(a, 'год')
else:
    print(a, 'лет')
