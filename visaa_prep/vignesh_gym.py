x1, x2, x3 = map(int, input().split())
if x3 < x1:
    print(0)
elif x3 >= x1 + x2:
    print(2)
else:
    print(1)
