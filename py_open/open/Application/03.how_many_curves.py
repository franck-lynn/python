import NXOpen
# import NXOpen_UF


def main():
    try:
        theSession = NXOpen.Session.GetSession()
        
        lw = theSession.ListingWindow
        lw.Open()
        
        numCurves = 0
        workPart = theSession.Parts.Work
        curves = workPart.Curves
        

        for cur in curves:
            numCurves = numCurves + 1
            curveLength = cur.GetLength()  #! 一般是大写开头
            lw.WriteLine('第' + str(numCurves) + "条曲线, 其长度为 " + str(curveLength))

        lw.WriteLine("总共有" + str(numCurves) + "条曲线")

    except Exception as ex:
        print(ex)


if __name__ == '__main__':
    main()
    pass
