#nx: threaded

import NXOpen
# import NXOpen_UF
import os

def main():
    # nx 的一些路径问题
    theSession = NXOpen.Session.GetSession()
    # theUI = NXOpen.UI.GetUI()
    # ufs = NXOpen_UF.UFSession.GetUFSession()
    
    lw = theSession.ListingWindow
    lw.Open()   
    lw.WriteLine("主程序入口的地址: ")   
    lw.WriteLine(os.getcwd())   
    lw.WriteLine("当前文件地址: ")   
    lw.WriteLine(os.path.abspath(__file__))   
    

if __name__ == '__main__':
    os.chdir("F:/working/study/yolanda/python/py_open/open/Application")
    main()