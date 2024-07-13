# 数组的内容
array = [2, 10, 6, 1, 12, 16, 9, 3, 4, 7, 14, 5, 11, 8, 15, 13]

# 找到所有可能的字符
chars = [chr(i) for i in list(range(48, 58)) + list(range(65, 91)) + list(range(97, 123))if (i & 0xf) < len(array)]

# 使用 itertools.product 生成所有可能的6个字符的字符串
from itertools import product
for s in product(chars, repeat=6):
    # 计算字符串的值
    value = sum(array[ord(c) & 0xf] for c in s)
    # 如果值等于60，打印字符串
    if value == 60:
        print(''.join(s))