def is_triangle(a, b, c):
    # 小到大排序
    side = [a, b, c]
    side = sorted(side)

    # 符合>=0 且 任兩邊相加大於第三邊的原則
    if side[2] <= 0 or side[0] + side[1] <= side[2]:
        return '這不是三角形'
    else:
        return '是三角形'


if __name__ == '__main__':
    print(is_triangle(3, 4, 8))
