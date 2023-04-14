def sum_divisible_by_3():
    total = 0
    for i in range(1, 31):
        if i % 3 == 0:
            total += i
    return total


result = sum_divisible_by_3()
print(result)
