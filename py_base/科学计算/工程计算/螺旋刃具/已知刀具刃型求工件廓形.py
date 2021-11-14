from sympy import *
# 定义参变量
from sympy.abc import u, x, y, z
# 定义符号变量
phi, R, A, sigma, p = symbols("phi, R, A, sigma, p")
# 定义  f(R) 方程
f = Function("f")
""" 
刀具回转面在 x1o1z1 坐标系中的方程, 其中:
R 参变数, 它表示 z1 对应的刀具回转面半径
phi 参变数, 它是半径 R 与 X1O1Z1 平面的夹角, 以 从 X1 轴转向 Y1 轴为正
"""
# 公式1
x1 = R * cos(phi)
y1 = R * sin(phi)
z1 = f(R)

# 公式2
x = x1 + A
y = y1 * cos(sigma) + z1 * sin(sigma)
z = -y1 * sin(sigma) + z1 * cos(sigma)  # 第1个负号表示左旋

# 对 公式2 分别对 R, phi 进行求导得到公式3
diff_x_derivative_R = x.diff(R)
diff_y_derivative_R = y.diff(R)
diff_z_derivative_R = z.diff(R)
diff_x_derivative_phi = x.diff(phi)
diff_y_derivative_phi = y.diff(phi)
diff_z_derivative_phi = z.diff(phi)

# 把 公式3 代法线矢量的偏微分方程, 用矩阵计算, 得到公式4
nx = simplify(Matrix(
    [
        [diff_y_derivative_R, diff_z_derivative_R],
        [diff_y_derivative_phi, diff_z_derivative_phi]
    ])
    .det())

ny = simplify(Matrix(
    [
        [diff_z_derivative_R, diff_x_derivative_R],
        [diff_z_derivative_phi, diff_x_derivative_phi]
    ])
    .det())

nz = simplify(Matrix(
    [
        [diff_x_derivative_R, diff_y_derivative_R],
        [diff_x_derivative_phi, diff_y_derivative_phi]
    ])
    .det())


""" 
把公式2 中的 x, y, z 和 公式4 的法向矢量分量 nx. ny, nz
代入螺旋面特性方程化简 nx * y - ny * x = -p * nz , 
同时, 方程的两边同除以 R * cos(sigma) * Derivative(f(R), R)) 并化简得, 
并命名 特性方程名称为 f1 
得到的结果如下:
(A + p*tan(sigma))*sin(phi) + (-A*tan(sigma) + p)/Derivative(f(R), R) + (-R/Derivative(f(R), R) - f(R))*cos(phi)*tan(sigma)
数学上的写法
(A + p tan(Σ)) sin(φ) - [f(R) + R / f'(R))] tan(Σ)cos(φ) -  1 / f'(R)  (A tan(sigma) -p) 
与手册上的写法一致
"""
f1 = simplify((nx * y - ny * x + p * nz) /
              (R * cos(sigma) * Derivative(f(R), R)))
f1 = collect(f1, sin(phi))  # 合并 sin(phi) 同类项

f1 = collect(f1, cos(phi)*tan(sigma))  # 合并 cos(phi)*tan(sigma) 同类项
f1 = collect(f1, 1 / Derivative(f(R), R))
""" 
f1 的方程式式刀具回转面的某点 M 成为接触点时, 两参变数
R, phi 满足的条件式, 取一个 R 值由上式解得对应的 phi 值, 
将求得的成对的 (R, phi) 值代入 公式2, 将此接触线绕工件
作螺旋运动就可以得到工件得螺旋面.
这个意思就是说: 
刀具回转面上某点 M(x, y, z), M 点与工件接触, M 点大部分不应该在平面内,
而是一个空间点, 

 """


# 测试程序
if __name__ == "__main__":
    # 把 公式 1 代入 公式2, 得到的结果与手册是一致的
    # print(x)
    # print(y)
    # print(z)
    #  公式2 对 R进行求导的结果
    # print(diff_x_derivative_R)
    # print(diff_y_derivative_R)
    # print(diff_z_derivative_R)
    #  公式2 对 phi 进行求导的结果
    # print(diff_x_derivative_phi)
    # print(diff_y_derivative_phi)
    # print(diff_z_derivative_phi)
    # 公式4 法向矢量分量
    # print(nx)
    # print(ny)
    # print(nz)
    # 化简后得公式
    print(f1)
