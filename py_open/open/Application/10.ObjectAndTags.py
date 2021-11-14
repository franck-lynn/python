# nx: threaded
import math
import NXOpen
import NXOpen.Features
import NXOpen.GeometricUtilities
import NXOpen.Preferences
# 1. 创建直线
# from nxobject.CreateLine import cteateLine
# 2. 创建草图函数
# from nxobject.Sketches01 import createSkecth
# 3. 创建草图类
# from nxobject.Sketches02 import Sketches02


def Sketches02():
    # 初始化
    try:
        theSession = NXOpen.Session.GetSession()
        workPart = theSession.Parts.Work
        
        lw = theSession.ListingWindow
        lw.Open()
        # lw.WriteLine("当前部件名称---> " + workPart.Name)
        
        
        # 1. 进入草图环境, 创建一个新草图平面构建器
        # newSchetch = NXOpen.Sketch.Null
        newSchetch = NXOpen.Sketch()
        # newSchetch.Name = "bbb"
        lw.WriteLine("草图---> " + str(dir(newSchetch)))
        # sketchBuilder = workPart.Sketches.CreateNewSketchInPlaceBuilder(NXOpen.Sketch.Null)
        # sketchBuilder = workPart.Sketches.CreateNewSketchInPlaceBuilder(newSchetch)

        # # 草图提交
        # sketchBuilder.Commit()
        # # 退出草图环境
        # sketchBuilder.Destroy()
        pass
    except Exception as ex:
        raise ex


if __name__ == '__main__':
    # cteateLine()
    # createSkecth()
    Sketches02()
    pass
