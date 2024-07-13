# def func4(x, low, high):
#     mid = (low + high) // 2
#     if mid == x:
#         return mid
#     elif mid < x:
#         return func4(x, mid + 1, high)
#     else:
#         return func4(x, low, mid - 1)

# def find_number():
#     for i in range(15):
#         if func4(i, 0, 14) == 21:
#             return i

# print(find_number())

def func4(x, low, high):
    mid = (low + high) // 2
    if mid < x:
        return func4(x, mid + 1, high)
    elif mid > x:
        return func4(x, low, mid - 1)
    else:
        return mid

def find_number():
    for i in range(15):
        if func4(i, 0, 14) == 21:
            return i

print(find_number())