def rotate_array(arr):
    n = len(arr)
    rotated_arr = [0] * n
    rotated_arr[0] = arr[-1]
    for i in range(1, n):
        rotated_arr[i] = arr[i-1]
    return rotated_arr


arr = [1, 2, 3, 4, 5]
rotated_arr = rotate_array(arr)
print(rotated_arr)
