# https://www.ugapi.com/doc/NXOpen/namespaces.html
# https://www.ugapi.com/thread-79.html
# http://www.nxopen.cn/thread-1248-1-1.html
import  NXOpen 
import  NXOpen_UF
# from sympy import *
def main():
    
    # 获取 NXOpen Session
    theSession = NXOpen.Session.GetSession()
    theUfSession = NXOpen_UF.UFSession.GetUFSession()
    print(theUfSession)
    # # 创建立方体
    # cornerPt = [0.0, 0.0, 0.0]
    # edgeLen = ["100.0", "50.0", "25.0"]
    # blockFeatTag = theUfSession
    
    # 获取 session 窗口列表
    lw = theSession.ListingWindow
    
    # 打开窗口列表
    lw.Open()
    # Get the name of the system log file
    logFileName = theSession.LogFile.FileName
    print(theSession, logFileName)
    pass


if __name__ == '__main__':
    main()
    pass
