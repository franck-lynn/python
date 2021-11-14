# nx: threaded
import abc  # 利用abc模块实现抽象类
import NXOpen
import NXOpen_UF


class NXObject(metaclass=abc.ABCMeta):
    theSession = None
    theUI = None

    def __init__(self, UIFilename) -> None:
        try:
            self.theSession = NXOpen.Session.GetSession()
            self.theUI = NXOpen.UI.GetUI()
            self.ufs = NXOpen_UF.UFSession.GetUFSession()

            # 构造函数传入 UI 的文件名称
            self.theDialog = self.theUI.CreateDialog(UIFilename)

            # 增加回调函数
            self.theDialog.AddApplyHandler(self.apply_cb)
            self.theDialog.AddOkHandler(self.ok_cb)
            self.theDialog.AddUpdateHandler(self.update_cb)
            self.theDialog.AddInitializeHandler(self.initialize_cb)
            self.theDialog.AddDialogShownHandler(self.dialogShown_cb)

        except Exception as ex:
            raise ex

    def Show(self):
        #! 01. 显示对话框
        try:
            self.theDialog.Show()
        except Exception as ex:
            # ---- Enter your exception handling code here -----
            self.theUI.NXMessageBox.Show(
                "Block Styler", NXOpen.NXMessageBox.DialogType.Error, str(ex))

    def Dispose(self):
        #! 02.释放内存函数
        if self.theDialog != None:
            self.theDialog.Dispose()
            self.theDialog = None

    # ------------------------------------------------------------------------------
    # ---------------------Block UI Styler Callback Functions--------------------------
    # ------------------------------------------------------------------------------
    @abc.abstractmethod
    def initialize_cb(self):
        # 初始化对话框的获取
        pass

    @abc.abstractmethod
    def dialogShown_cb(self):
        # 对话框显示时的回调函数
        pass

    # ! 三个按钮的回调函数

    @abc.abstractmethod
    def apply_cb(self):
        pass

    @abc.abstractmethod
    def update_cb(self):
        # 对话框失去焦点时的函数
        pass

    def cancel_cb(self):
        errorCode = 0
        try:
            # ---- Enter your callback code here -----
            pass
        except Exception as ex:
            # ---- Enter your exception handling code here -----
            errorCode = 1
            self.theUI.NXMessageBox.Show(
                "Block Styler", NXOpen.NXMessageBox.DialogType.Error, str(ex))
        return errorCode

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
