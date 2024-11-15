A = int(input())

if 3 <= A <= 5:
    print("Spring")
elif 6 <= A <= 8:
    print("Summer")
elif 9 <= A <= 11:
    print("Autumn")
elif A == 12 or 1 <= A <= 2:
    print("Winter")
else:
    print("Invalid")
