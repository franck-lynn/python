from functools import reduce

def fn(a, b):
    return a + b
    

print(reduce(fn, range(1, 101)))

print(True)
print(1)
print(1.0)
print(None)
print([1, 2, 3, 4])
print((1, 2, 3, 4))
print({"a":1, "b": 2})
print({"a",  "b" , "a"})