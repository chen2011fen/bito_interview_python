def array_diff(input_list1, input_list2):
    list1 = list(set(input_list1))
    list2 = list(set(input_list2))

    for i in reversed(range(len(list2))):
        if list2[i] in list1:
            list1.remove(list2[i])
            list2.remove(list2[i])
    result_list = sorted(list1 + list2)

    return result_list


if __name__ == '__main__':
    print(array_diff([2, 3, 4], [1, 2, 2, 2, 3, 3]))
