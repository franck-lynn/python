import NXOpen  


def main():
    try:
        theSession = NXOpen.Session.GetSession()

        lw = theSession.ListingWindow
        lw.Open()

        # lw.WriteLine('1. 获取的Session: ')
        # 主要就是  https://docs.plm.automation.siemens.com/data_services/resources/nx/10/nx_api/en_US/custom/nxopen_python_ref/NXOpen.Session.html#NXOpen.Session
        # Session 类里的东西
        # lw.WriteLine(str(dir(theSession)))
        # lw.WriteLine('2. ApplicationName 类 : ')
        
        # applicationName = theSession.ApplicationName
        # lw.WriteLine(str(dir(applicationName)))
        
        lw.WriteLine('3. Parts 类 : ')
        # https://docs.plm.automation.siemens.com/data_services/resources/nx/10/nx_api/en_US/custom/nxopen_python_ref/NXOpen.Part.html#NXOpen.Part
        parts = theSession.Parts.Work # 返回的是 Part class 
        # lw.WriteLine("工作部件 ---> " + str(dir(parts)))
        curves = parts.Curves
        # lw.WriteLine("工作部件里的曲线--->" + str(dir(curves)))
        
        numCurves = 0
        
        for cur in curves:
            numCurves = numCurves + 1
            curveLength = cur.GetLength()
            lw.WriteLine('第' + str(numCurves) + "条曲线, 其长度为 " + str(curveLength))
        
        
        lw.WriteLine("总共有" + str(numCurves) + "条曲线")
        # lw.WriteLine('4. CurveOperation 类 : ')
        # curveOperation = theSession.CurveOperation
        # lw.WriteLine(str(dir(curveOperation)))
        
        

    except Exception as ex:
        print(ex)


if __name__ == "__main__":
    main()
