#nx: threaded
# 使用 numpy 第3方库时要加上上面这句, 不然会非常非常卡顿
import numpy as np
import NXOpen
# import NXOpen_UF


def main():
    try:
        theSession = NXOpen.Session.GetSession()
        # theUfSession = NXOpen_UF.UFSession.GetUFSession()
        # NXOpen.UI.GetUI()

        lw = theSession.ListingWindow
        lw.Open()
        workPart = theSession.Parts.Work
        # # 需要的是浮点数
        # point1Coord = [50.0, -100.0, 0.0]
        # point2Coord = [50.0, 100.0, 0.0]

        # # 创建第1个点的符号
        # theUfSession.Curve.CreatePoint(point1Coord)
        # # 创建第2个点的符号
        # theUfSession.Curve.CreatePoint(point2Coord)

        # p1 =  NXOpen.Point3d(point1Coord[0], point1Coord[1], point1Coord[2])
        # p2 = NXOpen.Point3d(point2Coord[0], point2Coord[1], point2Coord[2])

        # line1 = workPart.Curves.CreateLine(p1, p2)

        # lw.WriteLine("创建的直线长度是 ---> " + str(line1.GetLength()))

        vertex = NXOpen.Point3d(0.0, 0.0, 0.0)
        focus = NXOpen.Point3d(100.0, 0.0, 0.0)
        axisX = NXOpen.Vector3d(1.0, 0.0, 0.0)
        axisY = NXOpen.Vector3d(0.0, 1.0, 0.0)

        focusLength = focus.X
        h = 100.0

        # 创建一段类圆弧曲线
        workPart.Curves.CreateParabola(vertex, axisX, axisY, focusLength, -h, h)

        # rangeY = range(-h, h, 10.0)
        rangeY = np.arange(-h, h + 1, 10.0)
        lw.WriteLine(str(rangeY))

        for y in rangeY:
            # 由于 x, y 的值是 np.float64 类型, 与 nx 不匹配, 所以要将类型转换一下
            y = np.float(y)
            x = (y * y) / (4.0 * focusLength)
            x = np.float(x)
            
            # lw.WriteLine(str(x) + "----" + str(y) + str(type(x)))
            p1 = NXOpen.Point3d(x, y, 0.0)
            p2 = NXOpen.Point3d(150.0, y, 0.0)
            # lw.WriteLine(str(p1))
            workPart.Curves.CreateLine(focus, p1)
            workPart.Curves.CreateLine(p1, p2)

    except Exception as ex:
        print(ex)


if __name__ == '__main__':
    main()
    pass
