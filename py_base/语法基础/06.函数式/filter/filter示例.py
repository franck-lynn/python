fn = lambda x: x < 3
lst = [1, 2, 3, 4, 5]
res = list(filter(fn, lst))
print(res)