# nx: threaded
# 使用 ui 文件
# import numpy as np
import NXOpen
import NXOpen_UF
# import sys
import os


class CreateBlock:
    # 静态成员变量
    theSession = None
    theUI = None
    # 构造函数

    def __init__(self) -> None:
        try:
            
            self.theSession = NXOpen.Session.GetSession()
            self.theUI = NXOpen.UI.GetUI()
            self.ufs = NXOpen_UF.UFSession.GetUFSession()

            self.theDlxFileName = "09.create_block.dlx"
            self.theDialog = self.theUI.CreateDialog(self.theDlxFileName)

            # 回调函数
            self.theDialog.AddUpdateHandler(self.update_cb)
            # ! 初始化对话框的回调函数, 什么时候调用这个函数? 打开对话框时就调用此回调函数
            self.theDialog.AddInitializeHandler(self.initialize_cb)
            self.theDialog.AddDialogShownHandler(self.dialogShown_cb)

            self.lw = self.theSession.ListingWindow
            self.lw.Open()

            # ! 在初始化时增加3个按钮的回调函数
            self.theDialog.AddOkHandler(self.ok_cb)
            self.theDialog.AddApplyHandler(self.apply_cb)
            self.theDialog.AddCancelHandler(self.cancel_cb)
            
            self.workPart = self.theSession.Parts.Work

        except Exception as ex:
            # ---- Enter your exception handling code here -----
            raise ex

    def initialize_cb(self):
        try:
            # self.lw.WriteLine("初始化时即调用此方法")
            self.group0 = self.theDialog.TopBlock.FindBlock("group0")
            # self.lw.WriteLine(str(self.group0))
            self.length = self.theDialog.TopBlock.FindBlock("length")
            self.lw.WriteLine(str(self.length.Value))
            self.width = self.theDialog.TopBlock.FindBlock("width")
            self.height = self.theDialog.TopBlock.FindBlock("height")

        except Exception as ex:
            self.theUI.NXMessageBox.Show(
                "Block Styler", NXOpen.NXMessageBox.DialogType.Error, str(ex))

    # ------------------------------------------------------------------------------
    # Callback Name: dialogShown_cb
    # This callback is executed just before the dialog launch. Thus any value set
    # here will take precedence and dialog will be launched showing that value.
    # ------------------------------------------------------------------------------
    def dialogShown_cb(self):
        try:
            # ---- Enter your callback code here -----
            self.lw.WriteLine("dialogShown_cb")
            pass
        except Exception as ex:
            # ---- Enter your exception handling code here -----
            self.theUI.NXMessageBox.Show(
                "Block Styler", NXOpen.NXMessageBox.DialogType.Error, str(ex))

    def apply_cb(self):
        errorCode = 0
        try:
            # ! 增加一个功能
            # ! 获取 leng, width, height 的值
            self.lw.WriteLine(str(self.length))
            self.lw.WriteLine(str(self.length.Value))
            self.lw.WriteLine(str(self.width.Value))
            self.lw.WriteLine(str(self.height.Value))
            # https://docs.plm.automation.siemens.com/data_services/resources/nx/10/nx_api/en_US/custom/nxopen_python_ref/NXOpen.UF.ModlFeatures.CreateBlock.html?highlight=createblock
            cornerPt =[0.0, 0.0, 0.0]
            edgeLen = [str(self.length.Value), str(self.width.Value), str(self.height.Value)]
            self.ufs.ModlFeatures.CreateBlock1(NXOpen_UF.Modl.FeatureSigns.NULLSIGN, cornerPt, edgeLen)
            
            pass
        except Exception as ex:
            # ---- Enter your exception handling code here -----
            errorCode = 1
            self.theUI.NXMessageBox.Show(
                "Block Styler", NXOpen.NXMessageBox.DialogType.Error, str(ex))
        return errorCode

    def Show(self):
        try:
            self.theDialog.Show()
        except Exception as ex:
            # ---- Enter your exception handling code here -----
            self.theUI.NXMessageBox.Show(
                "Block Styler", NXOpen.NXMessageBox.DialogType.Error, str(ex))

    #------------------------------------------------------------------------------
    # Callback Name: update_cb
    #------------------------------------------------------------------------------
    def update_cb(self, block):
        try:
            if block == self.length:
                # 修改长度值后, 该对话框失去焦点时执行
                self.lw.WriteLine("update_callback 执行")
                # ---- Enter your code here -----
                pass
            elif block == self.width:
                # ---- Enter your code here -----
                pass
            elif block == self.height:
                # ---- Enter your code here -----
                pass
        except Exception as ex:
            # ---- Enter your exception handling code here -----
            self.theUI.NXMessageBox.Show("Block Styler", NXOpen.NXMessageBox.DialogType.Error, str(ex))
        
        return 0


    def ok_cb(self):
        errorCode = 0
        try:
            errorCode = self.apply_cb()
        except Exception as ex:
            # ---- Enter your exception handling code here -----
            errorCode = 1
            self.theUI.NXMessageBox.Show(
                "Block Styler", NXOpen.NXMessageBox.DialogType.Error, str(ex))
        return errorCode

    def cancel_cb(self):
        errorCode = 0
        try:
            # ---- Enter your callback code here -----
            pass
        except Exception as ex:
            # ---- Enter your exception handling code here -----
            errorCode = 1
            self.theUI.NXMessageBox.Show(
                "Block Styler", NXOpen.NXMessageBox().DialogType.Error, str(ex))
        return errorCode

    # ------------------------------------------------------------------------------
    # Callback Name: enableOKButton_cb
    # This callback allows the dialog to enable/disable the OK and Apply button.
    # ------------------------------------------------------------------------------
    # def enableOKButton_cb(self):
    #     try:
    #         # ---- Enter your callback code here -----
    #         pass
    #     except Exception as ex:
    #         # ---- Enter your exception handling code here -----
    #         self.theUI.NXMessageBox.Show("Block Styler", NXOpen.NXMessageBox.DialogType.Error, str(ex))

    #     return True

    def Dispose(self):
        if self.theDialog != None:
            self.theDialog.Dispose()
            self.theDialog = None


def main():
    createBlock = None
    try:
        os.chdir("F:/working/study/yolanda/python/py_open/open/Application")
        createBlock = CreateBlock()
        createBlock.Show()
    except Exception as ex:
        # ---- Enter your exception handling code here -----
        NXOpen.UI.GetUI().NXMessageBox.Show(
            "Block Styler", NXOpen.NXMessageBox.DialogType.Error, str(ex))
    finally:
        if createBlock != None:
            createBlock.Dispose()
            createBlock = None


if __name__ == '__main__':
    main()
