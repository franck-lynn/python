# nx: threaded
import NXOpen
import NXOpen_UF
import os
import random

class BlockStylerRandomSpheres:
    theSession = None
    theUI = None

    def __init__(self):
        try:
            self.theSession = NXOpen.Session.GetSession()
            self.theUI = NXOpen.UI.GetUI()
            self.ufs = NXOpen_UF.UFSession.GetUFSession()
            
            self.theDlxFileName = "06.random_spheres.dlx"
            self.theDialog = self.theUI.CreateDialog(self.theDlxFileName)
            self.theDialog.AddApplyHandler(self.apply_cb)
            self.theDialog.AddOkHandler(self.ok_cb)
            self.theDialog.AddUpdateHandler(self.update_cb)
            self.theDialog.AddInitializeHandler(self.initialize_cb)
            self.theDialog.AddDialogShownHandler(self.dialogShown_cb)

        except Exception as ex:
            # ---- Enter your exception handling code here -----
            raise ex

    def Show(self):
        try:
            self.theDialog.Show()
        except Exception as ex:
            # ---- Enter your exception handling code here -----
            self.theUI.NXMessageBox.Show(
                "Block Styler", NXOpen.NXMessageBox.DialogType.Error, str(ex))

    def Dispose(self):
        if self.theDialog != None:
            self.theDialog.Dispose()
            self.theDialog = None

    def initialize_cb(self):
        try:
            self.readme = self.theDialog.TopBlock.FindBlock("readme")
            self.spheres_dia = self.theDialog.TopBlock.FindBlock(
                "spheres_dia")
        except Exception as ex:
            # ---- Enter your exception handling code here -----
            self.theUI.NXMessageBox.Show(
                "Block Styler", NXOpen.NXMessageBox.DialogType.Error, str(ex))

    def dialogShown_cb(self):
        try:
            # ---- Enter your callback code here -----
            pass
        except Exception as ex:
            # ---- Enter your exception handling code here -----
            self.theUI.NXMessageBox.Show(
                "Block Styler", NXOpen.NXMessageBox.DialogType.Error, str(ex))

    def apply_cb(self):
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
            # ---- Enter your exception handling code here -----
            errorCode = 1
            self.theUI.NXMessageBox.Show(
                "Block Styler", NXOpen.NXMessageBox.DialogType.Error, str(ex))

        return errorCode

    # ------------------------------------------------------------------------------
    # Callback Name: update_cb
    # ------------------------------------------------------------------------------
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

    # ------------------------------------------------------------------------------
    # Callback Name: ok_cb
    # ------------------------------------------------------------------------------
    def ok_cb(self):
        errorCode = 0
        try:
            # ---- Enter your callback code here -----
            errorCode = self.apply_cb()
        except Exception as ex:
            # ---- Enter your exception handling code here -----
            errorCode = 1
            self.theUI.NXMessageBox.Show(
                "Block Styler", NXOpen.NXMessageBox.DialogType.Error, str(ex))

        return errorCode


def main():
    os.chdir("F:/working/study/yolanda/python/py_open/open/Application")
    theBlockStyler06random_spheres = None
    try:
        theBlockStyler06random_spheres = BlockStylerRandomSpheres()
        #  The following method shows the dialog immediately
        theBlockStyler06random_spheres.Show()
    except Exception as ex:
        # ---- Enter your exception handling code here -----
        NXOpen.UI.GetUI().NXMessageBox.Show(
            "Block Styler", NXOpen.NXMessageBox.DialogType.Error, str(ex))
    finally:
        if theBlockStyler06random_spheres != None:
            theBlockStyler06random_spheres.Dispose()
            theBlockStyler06random_spheres = None


if __name__ == '__main__':
    main()
