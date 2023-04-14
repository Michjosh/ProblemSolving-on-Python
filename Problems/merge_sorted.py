def merge_sorted_lists(list1, list2):
    i = 0
    j = 0
    merged_lists = []

    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged_lists.append(list1[i])
            i += 1
        else:
            merged_lists.append(list2[j])
            j += 1

    merged_lists += list1[i:]
    merged_lists += list2[j:]

    return merged_lists


list1 = [1, 3, 4, 5]
list2 = [2, 6, 7, 8]

merged_list = merge_sorted_lists(list1, list2)

print(merged_list)
