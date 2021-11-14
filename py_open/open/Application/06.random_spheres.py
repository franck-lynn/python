# nx: threaded
import NXOpen
import NXOpen_UF
import os
import random
from nxobject.NXObject import NXObject

#! 回调函数需要按照一定的顺序? 否则报内存违规用例错误?
class RandomSpheres(NXObject):
    theSession = None
    theUI = None

    def __init__(self, UIFilename):
        try:

            super().__init__(UIFilename)

            self.lw = self.theSession.ListingWindow
            self.lw.Open()
        except Exception as ex:
            # ---- Enter your exception handling code here -----
            raise ex

    #! Show 函数继承
    #! Dispose() 函数继承

    def initialize_cb(self):
        #! 1. 覆写初始化函数
        try:
            self.readme = self.theDialog.TopBlock.FindBlock("readme")
            self.spheres_dia = self.theDialog.TopBlock.FindBlock(
                "spheres_dia")
        except Exception as ex:
            self.theUI.NXMessageBox.Show(
                "Block Styler", NXOpen.NXMessageBox.DialogType.Error, str(ex))

    # 注册不了这个函数
    # def handleCreateSpheres_cb(self):
    #     self.lw.WriteLine("处理自定义的")

    def dialogShown_cb(self):
        #! 2. 覆写dialogShown_cb函数
        try:
            # 对话框显示时执行
            # self.lw.WriteLine("调用 dialogShow, 获取双精度款中的值: " + str(self.spheres_dia.Value))
            pass
        except Exception as ex:
            # ---- Enter your exception handling code here -----
            self.theUI.NXMessageBox.Show(
                "Block Styler", NXOpen.NXMessageBox.DialogType.Error, str(ex))

    

    def apply_cb(self):
        #! 4. 覆写 apply_cb 函数
        # self.lw.WriteLine("调用 apply_cb")
        errorCode = 0
        try:
            for i in range(100):
                # self.lw.WriteLine("调用 apply_cb")
                # 在这个函数里生成随机球
                x = 100 * random.random()
                y = 100 * random.random()
                z = 100 * random.random()
                spheres_dia = self.spheres_dia.Value
                self.ufs.ModlFeatures.CreateSphere1(NXOpen_UF.Modl.FeatureSigns.NULLSIGN, [
                                                    x, y, z], str(spheres_dia))
        except Exception as ex:
            errorCode = 1
            self.theUI.NXMessageBox.Show(
                "Block Styler", NXOpen.NXMessageBox.DialogType.Error, str(ex))
        return errorCode
       
    def update_cb(self, block):
        try:
            if block == self.readme:
                # ---- Enter your code here -----
                pass
            elif block == self.spheres_dia:
                # ---- Enter your code here -----
                pass
        except Exception as ex:
            # ---- Enter your exception handling code here -----
            self.theUI.NXMessageBox.Show(
                "Block Styler", NXOpen.NXMessageBox.DialogType.Error, str(ex))

        return 0
        
    #! 5. cancel_cb 函数继承
    #! 6. ok_cb 函数继承


def main(UIFilename):
    nxObject = None
    try:
        os.chdir("F:/working/study/yolanda/python/py_open/open/Application")
        nxObject = RandomSpheres(UIFilename)
        nxObject.Show()
    except Exception as ex:
        # ---- Enter your exception handling code here -----
        NXOpen.UI.GetUI().NXMessageBox.Show(
            "Block Styler", NXOpen.NXMessageBox.DialogType.Error, str(ex))
    finally:
        if nxObject != None:
            nxObject.Dispose()
            nxObject = None


if __name__ == '__main__':
    main("06.random_spheres.dlx")
