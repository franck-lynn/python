# NX 1980
# Journal created by lynn on Sat Oct 30 23:11:18 2021 中国标准时间

#
import math
import NXOpen
import NXOpen.Features
import NXOpen.GeometricUtilities
import NXOpen.Preferences
def main() : 

    theSession  = NXOpen.Session.GetSession()
    workPart = theSession.Parts.Work
    displayPart = theSession.Parts.Display
    # ----------------------------------------------
    #   菜单：插入(S)->草图(S)
    # ----------------------------------------------
    markId1 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Enter Sketch")
    
    markId2 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Update Model from Sketch")
    
    theSession.BeginTaskEnvironment()
    workPart.Sketches
    # ----------------------------------------------
    #   菜单：应用模块(N)->文档(E)->PMI
    # ----------------------------------------------
    markId3 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "起点")
    
    sketchInPlaceBuilder1 = workPart.Sketches.CreateSketchInPlaceBuilder2(NXOpen.Sketch.Null)
    
    origin1 = NXOpen.Point3d(0.0, 0.0, 0.0)
    normal1 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    plane1 = workPart.Planes.CreatePlane(origin1, normal1, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    sketchInPlaceBuilder1.PlaneReference = plane1
    
    unit1 = workPart.UnitCollection.FindObject("MilliMeter")
    expression1 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression2 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    sketchInPlaceBuilder1.OriginOption = NXOpen.OriginMethod.WorkPartOrigin
    
    sketchInPlaceBuilder1.OriginOptionInfer = NXOpen.OriginMethod.WorkPartOrigin
    
    sketchAlongPathBuilder1 = workPart.Sketches.CreateSketchAlongPathBuilder(NXOpen.Sketch.Null)
    
    simpleSketchInPlaceBuilder1 = workPart.Sketches.CreateSimpleSketchInPlaceBuilder()
    
    sketchInPlaceBuilder1.OriginOptionInfer = NXOpen.OriginMethod.SpecifyPoint
    
    sketchInPlaceBuilder1.OriginOption = NXOpen.OriginMethod.SpecifyPoint
    
    sketchAlongPathBuilder1.PlaneLocation.Expression.SetFormula("0")
    
    theSession.SetUndoMarkName(markId3, "创建草图 对话框")
    
    simpleSketchInPlaceBuilder1.UseWorkPartOrigin = True
    
    markId4 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "创建草图")
    
    theSession.DeleteUndoMark(markId4, None)
    
    markId5 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "创建草图")
    
    origin2 = NXOpen.Point3d(0.0, 0.0, 0.0)
    vector1 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    direction1 = workPart.Directions.CreateDirection(origin2, vector1, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    coordinates1 = NXOpen.Point3d(0.0, 0.0, 0.0)
    point1 = workPart.Points.CreatePoint(coordinates1)
    
    origin3 = NXOpen.Point3d(0.0, 0.0, 0.0)
    matrix1 = NXOpen.Matrix3x3()
    
    matrix1.Xx = 1.0
    matrix1.Xy = 0.0
    matrix1.Xz = 0.0
    matrix1.Yx = 0.0
    matrix1.Yy = 1.0
    matrix1.Yz = 0.0
    matrix1.Zx = 0.0
    matrix1.Zy = 0.0
    matrix1.Zz = 1.0
    plane2 = workPart.Planes.CreateFixedTypePlane(origin3, matrix1, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    xform1 = workPart.Xforms.CreateXformByPlaneXDirPoint(plane2, direction1, point1, NXOpen.SmartObject.UpdateOption.WithinModeling, 1.0, False, False)
    
    cartesianCoordinateSystem1 = workPart.CoordinateSystems.CreateCoordinateSystem(xform1, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    simpleSketchInPlaceBuilder1.CoordinateSystem = cartesianCoordinateSystem1
    
    theSession.Preferences.Sketch.CreateInferredConstraints = True
    
    theSession.Preferences.Sketch.ContinuousAutoDimensioning = False
    
    theSession.Preferences.Sketch.DimensionLabel = NXOpen.Preferences.SketchPreferences.DimensionLabelType.Expression
    
    theSession.Preferences.Sketch.TextSizeFixed = True
    
    theSession.Preferences.Sketch.FixedTextSize = 5.0
    
    theSession.Preferences.Sketch.DisplayParenthesesOnReferenceDimensions = False
    
    theSession.Preferences.Sketch.DisplayReferenceGeometry = True
    
    theSession.Preferences.Sketch.DisplayShadedRegions = True
    
    theSession.Preferences.Sketch.FindMovableObjects = True
    
    theSession.Preferences.Sketch.ConstraintSymbolSize = 3.0
    
    theSession.Preferences.Sketch.DisplayObjectColor = False
    
    theSession.Preferences.Sketch.DisplayObjectName = True
    
    theSession.Preferences.Sketch.EditDimensionOnCreation = True
    
    nXObject1 = simpleSketchInPlaceBuilder1.Commit()
    
    sketch1 = nXObject1
    feature1 = sketch1.Feature
    
    markId6 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "update")
    
    nErrs1 = theSession.UpdateManager.DoUpdate(markId6)
    
    sketch1.Activate(NXOpen.Sketch.ViewReorient.TrueValue)
    
    theSession.DeleteUndoMark(markId5, None)
    
    theSession.SetUndoMarkName(markId3, "创建草图")
    
    sketchInPlaceBuilder1.Destroy()
    
    sketchAlongPathBuilder1.Destroy()
    
    simpleSketchInPlaceBuilder1.Destroy()
    
    try:
        # 表达式仍然在使用中。
        workPart.Expressions.Delete(expression2)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    try:
        # 表达式仍然在使用中。
        workPart.Expressions.Delete(expression1)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    plane1.DestroyPlane()
    
    theSession.DeleteUndoMarksUpToMark(markId2, None, True)
    
    markId7 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Open Sketch")
    
    theSession.ActiveSketch.SetName("SKETCH_000")
    
    markId8 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Profile short list")
    
    # ----------------------------------------------
    #   对话开始 轮廓
    # ----------------------------------------------
    # ----------------------------------------------
    #   菜单：插入(S)->曲线(C)->圆弧(A)...
    # ----------------------------------------------
    theSession.DeleteUndoMark(markId8, "Curve")
    
    markId9 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Profile short list")
    
    markId10 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Curve")
    
    theSession.SetUndoMarkVisibility(markId10, "Curve", NXOpen.Session.MarkVisibility.Visible)
    
    nXMatrix1 = theSession.ActiveSketch.Orientation
    
    center1 = NXOpen.Point3d(0.0, 0.0, 0.0)
    arc1 = workPart.Curves.CreateArc(center1, nXMatrix1, 53.805640947752117, 0.0, ( 176.01049288737713 * math.pi/180.0 ))
    
    theSession.ActiveSketch.AddGeometry(arc1, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    geom1_1 = NXOpen.Sketch.ConstraintGeometry()
    
    geom1_1.Geometry = arc1
    geom1_1.PointType = NXOpen.Sketch.ConstraintPointType.ArcCenter
    geom1_1.SplineDefiningPointIndex = 0
    geom2_1 = NXOpen.Sketch.ConstraintGeometry()
    
    datumCsys1 = workPart.Features.FindObject("SKETCH(10:1B)")
    point2 = datumCsys1.FindObject("POINT 1")
    geom2_1.Geometry = point2
    geom2_1.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    geom2_1.SplineDefiningPointIndex = 0
    sketchGeometricConstraint1 = theSession.ActiveSketch.CreateCoincidentConstraint(geom1_1, geom2_1)
    
    theSession.ActiveSketch.Update()
    
    # ----------------------------------------------
    #   对话开始 圆弧
    # ----------------------------------------------
    # ----------------------------------------------
    #   菜单：任务(K)->完成草图(K)
    # ----------------------------------------------
    theSession.Preferences.Sketch.SectionView = False
    
    markId11 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Deactivate Sketch")
    
    theSession.ActiveSketch.Deactivate(NXOpen.Sketch.ViewReorient.TrueValue, NXOpen.Sketch.UpdateLevel.Model)
    
    theSession.DeleteUndoMarksSetInTaskEnvironment()
    
    # ----------------------------------------------
    #   菜单：应用模块(N)->文档(E)->PMI
    # ----------------------------------------------
    theSession.EndTaskEnvironment()
    
    # ----------------------------------------------
    #   菜单：工具(T)->操作记录(J)->停止录制(S)
    # ----------------------------------------------
    
if __name__ == '__main__':
    main()