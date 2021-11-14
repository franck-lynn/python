
a = set('abcdmn')
b = set('aefgmn')

# 集合并差交补
print("并", a | b)
print("交", a & b)
print("差", a - b) # a 差 b 是保留 a
print(b - a)
print(b ^ a)

print("差", a.difference(b))
print("交", a.intersection(b))
print("并", a.union(b))
