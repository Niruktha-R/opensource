def is_arr_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True
no = int(input())
arr = list(map(int, input().split()))
print("true" if is_arr_sorted(arr) else "false")
