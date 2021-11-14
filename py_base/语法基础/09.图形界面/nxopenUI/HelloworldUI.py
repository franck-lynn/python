# nx: threaded
import NXOpen
import NXOpen_UF
import os

def helloworldUI():
    try:
        # 尝试创建一个 PyQt5 的对话框
        theSession = NXOpen.Session.GetSession()
        theUI = NXOpen.UI.GetUI()
        NXOpen.UI.Styler
        lw = theSession.ListingWindow
        lw.Open()

        # 调用创建对话框函数, 调用第三方的 ui 不行, 提示要 dlx 文件
        # NXOpen.NXException: 用于块 UI 样式编辑器对话框文件的文件扩展名 * 无效。使用 dlx 扩展名。
        # theDialog = theUI.CreateDialog('./HelloworldUI.ui')
        # 只能通过PyQt6的线程调用对话框, 再传入 NX
        lw.WriteLine(str("theDialog"))
        
        
        pass
    except Exception as ex:
        raise ex



if __name__ == '__main__':
    os.chdir("F:/working/study/yolanda/python/py_base/09.图形界面/nxopenUI")
    helloworldUI()
    pass