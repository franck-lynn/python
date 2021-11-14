t1 = ('Google', 'Runoob', 1997, 2000)
t2 = (1, 2, 3, 4, 5, 6, 7 )

print(t1[0], t2[1:5])

# 遍历
for i in t1:
    print(i)
    
    
# 修改. 非法
t1[0] = "aaa"