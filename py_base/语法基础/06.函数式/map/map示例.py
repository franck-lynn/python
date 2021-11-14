lst = [(1,2),(3,5),(6,3),(2,6),(2,5)]

# 返回元组的第1项
def first(a: tuple):
    return a[0]
    
res = list(map(first, lst))

print(res)