def highest_and_lowest(input_list):
    try:
        # 小到大排序
        list = sorted(input_list)
        # 取出第一個(最小)和最後一個(最大)的值
        return f'lowest number:{list[0]}, highest number:{list[-1]}'
    except TypeError:
        return '僅能輸入數字陣列'


if __name__ == '__main__':
    print(highest_and_lowest([0, 8, 5, -10, -3]))
