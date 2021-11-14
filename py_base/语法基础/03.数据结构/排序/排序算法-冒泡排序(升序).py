nums = [56, 30, 12, 9, 8]
# print(len(nums))
# 5 个数组要比较 4 次, len(nums) = 5, len(nums) -1 = 4, 不包括 4,  (0, 1, 2, 3) 正好是4次循环


# def exchange(nums):
#     for j in range(0, len(nums) - 1):
#         if nums[j] > nums[j + 1]:
#             nums[j], nums[j + 1] = nums[j + 1], nums[j]
#     print(nums)

# 交换 4次就可以完整排序了
# exchange(nums)
# exchange(nums)
# exchange(nums)
# exchange(nums)

# 冒泡排序
# def bubble(nums):
#     for i in range(0, len(nums) - 1):
#         for j in range(0, len(nums) - 1):
#             if nums[j] > nums[j + 1]:
#                 nums[j], nums[j + 1] = nums[j + 1], nums[j]
#         print(nums)


# bubble(nums)


# 冒泡排序
def bubble_optimize(nums):
    for i in range(0, len(nums) - 1):
        # 更少的比较次数, 对于升序, 最后已经排好了, 只要前面的数组排序就可以了, 减少排序次数
        for j in range(0, len(nums) - 1 - i):
            if nums[j] > nums[j + 1]:
                # 后面的小就调到前面来
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
        print(nums)


bubble_optimize(nums)


print("*" * 50)


def bubble_optimize1(nums):
    for i in range(0, len(nums) - 1):
        # 更少的比较次数, 对于升序, 从前面开始先排
        for j in range(i, len(nums) - 1):
            if nums[j] > nums[j + 1]:
                # 后面的大就调到前面来
                nums[j + 1], nums[j],  = nums[j], nums[j + 1]
        print(nums)


bubble_optimize1(nums)

print("*" * 50)


