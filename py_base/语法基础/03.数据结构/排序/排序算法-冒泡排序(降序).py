
nums = [8, 9, 12, 30, 56]

# def exchange_desccending_order(nums):
#     for j in range(0, len(nums) - 1):
#         if nums[j] < nums[j + 1]:
#             nums[j], nums[j + 1] = nums[j + 1], nums[j]
#     print(nums) 
    
# exchange_desccending_order(nums)
# exchange_desccending_order(nums)
# exchange_desccending_order(nums)
# exchange_desccending_order(nums)


# def bubble_desccending_order(nums):
#     for i in range(0, len(nums) - 1):
#         for j in range(0, len(nums) - 1):
#             if nums[j] < nums[j + 1]:
#                 nums[j], nums[j + 1] = nums[j + 1], nums[j]
#         print(nums)

# bubble_desccending_order(nums)



def bubble_optimize_desccending_order(nums):
    for i in range(0, len(nums) - 1):
        # 更少的比较次数
        for j in range(0, len(nums) - 1 - i):
            if nums[j] < nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
        print(nums)


bubble_optimize_desccending_order(nums)