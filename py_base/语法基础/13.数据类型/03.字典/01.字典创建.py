d = {'name': 'runoob', 'likes': 123, 'url': 'www.runoob.com'}
print("字典: ", d)


# 创建一个新字典
d1 = {}
d2 = d1.fromkeys("x", "value")
print(d2)
print(d2.get('x'))

print("以列表形式返回一个字典", d2.items())
print("以列表形式返回一个字典的键", d2.keys())
