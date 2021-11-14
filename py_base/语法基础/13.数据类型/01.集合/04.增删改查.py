a = set()

print(a)
a.add('google')
print(a)
# update 必须是元组或者字典, 列表, 集合中添加多个元素
a.update(['runoob', 'taobao'])
print(a)

# 删除
# a.remove('google')
# print(a)
a.discard('google')
print(a)
print("*" * 50)
a = set(("Google", "Runoob", "Taobao", "Facebook"))
a.pop()  # 随机弹出, 因为集合是无序的
print(a)

# 清空
a.clear()
print(a)