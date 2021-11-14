import math
import NXOpen
import NXOpen.Features
import NXOpen.GeometricUtilities
import NXOpen.Preferences
# https://www.bilibili.com/video/BV1FU4y1L7ow?from=search&seid=6178460982746980451&spm_id_from=333.337.0.0


class Sketches02:
    def __init__():
        try:
            theSession = NXOpen.Session.GetSession()
            workPart = theSession.Parts.Work

            lw = theSession.ListingWindow
            lw.Open() 
            
            sketchBuilder = workPart.Sketches.CreateNewSketchInPlaceBuilder(NXOpen.Sketch.Null)
            # sketchBuilder = workPart.Sketches.CreateNewSketchInPlaceBuilder(newSchetch)

            # 草图提交
            sketchBuilder.Commit()
            # 退出草图环境
            sketchBuilder.Destroy()
            pass
        except Exception as ex:
            raise ex
