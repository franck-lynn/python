import math
import NXOpen
import NXOpen.Features
import NXOpen.GeometricUtilities
import NXOpen.Preferences


def createSkecth():
    try:
        theSession = NXOpen.Session.GetSession()
        workPart = theSession.Parts.Work
        # lw = theSession.ListingWindow
        # lw.Open()
        # lw.WriteLine("当前部件名称---> " + workPart.Name)

        # 草图的坐标原点
        origin = NXOpen.Point3d(0.0, 0.0, 0.0)
        # 草图的法线矢量, 垂直于这个矢量的平面就是草图平面
        normal = NXOpen.Vector3d(0.0, 0.0, 1.0)
        # 生成草绘平面
        sketchPlane = workPart.Planes.CreatePlane(origin, normal,  NXOpen.SmartObject.UpdateOption.WithinModeling)
        

        # 返回 SketchInPlaceBuilder
        sketchBuilder = workPart.Sketches.CreateNewSketchInPlaceBuilder(NXOpen.Sketch.Null)

        sketchBuilder.PlaneOrFace.Value = sketchPlane
        
        sketchBuilder.SketchOrigin = workPart.Points.CreatePoint(origin)
        sketchBuilder.PlaneOption = NXOpen.Sketch.PlaneOption.Inferred
        # 提交返回一个对象 NXOpen.NXObject
        bridgeSketch = sketchBuilder.Commit()
        sketchBuilder.Destroy()
        # https://docs.plm.automation.siemens.com/data_services/resources/nx/10/nx_api/en_US/custom/nxopen_python_ref/NXOpen.Sketch.html?highlight=activate#nxopen-sketch-addgeometry
        bridgeSketch.Activate(NXOpen.SketchViewReorient.TrueValue)

        p0 = NXOpen.Point3d(2.0, 0.0, 0.0)
        p1 = NXOpen.Point3d(0.0, 0.0, 0.0)
        pm = NXOpen.Point3d(1.0, 1.0, 0.0)
        gotFlipped = False
        # CreateArc(圆弧起点, 圆弧通过点, 圆弧终点, 替代解决方案(如果常规解决方案是从 0 度到 45 度的弧，则替代解决方案将是具有相同中心和原点但从 45 度到 360 度的弧)), 返回的是一个元组
        bridge = workPart.Curves.CreateArc(p1, theSession.ActiveSketch.Orientation, 10.0, 0.0, math.pi * 3 / 4)

        # 添加对象到草图, 不推断约束
        bridgeSketch.AddGeometry(
            bridge, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
        pass
    except Exception as ex:
        raise ex

