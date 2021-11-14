# impreative programming 命令式
# a = 0
# def incrementI():
#     global a
#     a += 1

def first(a: tuple):
    return a[0]


lst = [(1, 2), (3, 5), (6, 3), (2, 6), (2, 5)]
# map 取出每个元素, first 函数进行处理
# 这里需要list()来强迫Python计算以便看到结果，因为Python3以后，map变成惰性函数了
# 也就是变成Generator了
res = list(map(first, lst))

print(res)

from functools import reduce


lst = [1, 2, 3, 4, 5]
print(list(filter(lambda x: x < 3, lst)))


sentences = ['Mary read a story to Sam and Isla.',
             'Isla cuddled Sam.',
             'Sam chortled.']

# sam_count = 0
# for s in sentences:
#     sam_count += s.count('Sam')

# print(sam_count)


def count(pre_count: int, new_item) -> int:
    return pre_count + new_item.count('Sam')


sam_count = reduce(count, sentences, 0)
print(sam_count)

# https://zhuanlan.zhihu.com/p/88198966

people = [{'name': 'Mary', 'height': 160},
          {'name': 'Isla', 'height': 80},
          {'name': 'Sam'}]

# 先找出全部身高,  map 第2个参数是 list
heights = list(map(lambda x : x['height'], filter(lambda x : 'height' in x, people)))
# print(list(heights))
average_height = reduce(lambda a, b:  a + b, heights, 0) / len(heights)

print(average_height)













